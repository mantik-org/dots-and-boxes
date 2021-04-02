import logging
import asyncio
import websockets
import json
import sys

from ..ai.remote import on_start
from ..ai.remote import on_action
from ..ai.remote import on_end

logger = logging.getLogger(__name__)

class Game:

    __instance__ = None

    def __init__(self):
        self.matches = []


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
                on_start(Game.getInstance(), data)
            
            elif data['type'] == 'action':
                on_action(Game.getInstance(), data)

            elif data['type'] == 'end':
                on_end(Game.getInstance(), data)

            else:
                logger.info('[WEBSOCK] Received invalid type {}'.format(data['type']))

        except:
            pass


    def run(self, host, port):

        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.StreamHandler(sys.stderr))

        logger.info('[GAME] Running...')

        server = websockets.serve(Game.on_network_data, host, port)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()

