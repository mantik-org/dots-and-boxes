import logging
import sys

from .core.game import Game


def main():

    logger = logging.getLogger('debug')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stderr))
    
    Game.getInstance().run('localhost', 8081)

if __name__ == '__main__':
    main()