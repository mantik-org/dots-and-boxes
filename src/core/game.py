#                                                                      
# GPL3 License 
#
# Author(s):                                                              
#      Antonino Natale <ntlnnn97r06e041t@studenti.unical.it>
#      Matteo Perfidio <prfmtt98e07f537p@studenti.unical.it>
# 
# 
# Copyright (C) 2021 Mantik
#
# This file is part of DotsAndBoxesAI.  
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

import logging
import asyncio
import websockets
import json
import sys
import traceback

from src.core.game_match import GameMatch
from src.ai.agents.agent import Agent


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
                    Game.getInstance().init_match(data['game'], data['player'], data['grid'], websocket)
                
                elif data['type'] == 'action':
                    Game.getInstance().update_match(data['game'], data['player'], data['location'], data['orientation'], data['nextplayer'], data['score'])

                elif data['type'] == 'end':
                    pass

                else:
                    logger.info('[WEBSOCK] Received invalid type {}'.format(data['type']))

        except Exception as e:
            logger.error('[NETWORK] Exception {}'.format(e))
            traceback.print_exc()


    def init_match(self, identifier, player, grid, socket):


        if not identifier in self.matches:
            logger.info("[GAME] Starting new match ({}) with grid {}".format(identifier, grid))
            self.matches[identifier] = GameMatch(identifier, grid)


        self.matches[identifier].add_player(player, socket)
        
        if player == 1:
            self.matches[identifier].play(self, 1)
            

    def update_match(self, match, player, location, orientation, nextplayer = None, score = None, remote = False):
        
        if not match in self.matches:
            logger.error('[GAME] Match not found: <{}>'.format(match))
            return

        logger.info('[GAME] Update board at {}:{} from {} / score: {}, nextplayer: {}, remote: {}'.format(location, orientation, player, score, nextplayer, remote))


        self.matches[match].prepare(self, nextplayer)

        rows, cols = location
        self.matches[match].board[rows][cols][orientation] = player

        if score is not None:
            self.matches[match].score = score
        
        if nextplayer is not None:
            self.matches[match].play(self, nextplayer)

        if remote:
            asyncio.get_event_loop().create_task(
                self.matches[match].players[player].socket.send(json.dumps({
                    'type'          : 'action',
                    'location'      : location,
                    'orientation'   : str(orientation)
                }))
            )


    def run(self, host, port):

        logger.info('[GAME] Running')
        Agent.initMappings()


        self.server = websockets.serve(Game.on_network_data, port=port)

        logger.info('[NETWORK] Listening on {}:{}...'.format(host, port))
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

