import logging
import asyncio
import websockets
import json
import sys

from .game_match import GameMatch

logger = logging.getLogger('debug')

class Game:

    __instance__ = None

    def __init__(self):
        self.matches = {}


    @staticmethod
    def getInstance():
        if Game.__instance__ is None:
            Game.__instance__ = Game()
        return Game.__instance__


    @staticmethod
    async def on_network_data(websocket, path):
        try:          
            async for data in websocket:

                logger.debug('[WEBSOCK] Received {}'.format(data))

                try:
                    data = json.loads(data)
                except json.decoder.JSONDecodeError as e:
                    logger.error(e)
                    return False

                if data['type'] == 'start':
                    Game.getInstance().init_match(data['game'], data['player'], data['grid'])
                
                elif data['type'] == 'action':
                    Game.getInstance().update_match(data['game'], data['player'], data['nextplayer'], data['score'], data['location'], data['orientation'])

                elif data['type'] == 'end':
                    pass

                else:
                    logger.info('[WEBSOCK] Received invalid type {}'.format(data['type']))

        except:
            pass


    def init_match(self, identifier, player, grid):


        if not identifier in self.matches:
            logger.info("[GAME] Starting new match ({}) with grid {}".format(identifier, grid))
            self.matches[identifier] = GameMatch(identifier, grid)


        self.matches[identifier].add_player(player)
        
        if player == 1:
            self.matches[identifier].play(1)
            

    def update_match(self, match, player, nextplayer, score, location, orientation):
        
        if not match in self.matches:
            logger.error('[GAME] Match not found: <{}>'.format(match))
            return

        logger.info('[GAME] Update board at {}:{} from {} / score: {}, nextplayer: {}'.format(location, orientation, player, score, nextplayer))

        rows, cols = location
        self.matches[match].score = score
        self.matches[match].board[rows][cols][orientation] = player
        self.matches[match].play(nextplayer)


    def run(self, host, port):

        logger.info('[GAME] Running...')

        server = websockets.serve(Game.on_network_data, host, port)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()

