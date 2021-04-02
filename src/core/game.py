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
        self.websocket = None


    @staticmethod
    def getInstance():
        if Game.__instance__ is None:
            Game.__instance__ = Game()
        return Game.__instance__


    @staticmethod
    async def on_network_data(websocket, path):

        Game.getInstance().websocket = websocket

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
                    Game.getInstance().update_match(data['game'], data['player'], data['location'], data['orientation'], data['nextplayer'], data['score'])

                elif data['type'] == 'end':
                    pass

                else:
                    logger.info('[WEBSOCK] Received invalid type {}'.format(data['type']))

        except Exception as e:
            logger.error('[NETWORK] Exception {}'.format(e))


    def init_match(self, identifier, player, grid):


        if not identifier in self.matches:
            logger.info("[GAME] Starting new match ({}) with grid {}".format(identifier, grid))
            self.matches[identifier] = GameMatch(identifier, grid)


        self.matches[identifier].add_player(player)
        
        if player == 1:
            self.matches[identifier].play(self, 1)
            

    def update_match(self, match, player, location, orientation, nextplayer = None, score = None, remote = False):
        
        if not match in self.matches:
            logger.error('[GAME] Match not found: <{}>'.format(match))
            return

        logger.info('[GAME] Update board at {}:{} from {} / score: {}, nextplayer: {}, remote: {}'.format(location, orientation, player, score, nextplayer, remote))

        rows, cols = location
        self.matches[match].board[rows][cols][orientation] = player

        if score is not None:
            self.matches[match].score = score
        
        if nextplayer is not None:
            self.matches[match].play(self, nextplayer)

        if remote and self.websocket is not None:
            asyncio.get_event_loop().create_task(
                self.websocket.send(json.dumps({
                    'type'          : 'action',
                    'location'      : location,
                    'orientation'   : str(orientation)
                }))
            )


    def run(self, host, port):

        logger.info('[GAME] Running...')

        self.server = websockets.serve(Game.on_network_data, host, port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

