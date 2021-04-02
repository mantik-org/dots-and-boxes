
import logging

logger = logging.getLogger('debug')

class GameMatch:

    def __init__(self, identifier, grid):

        rows, cols = grid

        self.identifier = identifier
        self.rows = rows
        self.cols = cols
        self.board = []
        self.players = {}

        for _ in range(rows + 1):
            col = []
            for _ in range(cols + 1):
                col.append({ 'v' : 0, 'h': 0 })
            self.board.append(col)


    def add_player(self, identifier):
        logger.info('[GAME] Registered new player {} in match <{}>'.format(identifier, self.identifier))
        # if not identifier in self.players:
        #   self.players[identifier] = PlayerAgent(identifier, self)
        pass


    def play(self, identifier):

        if identifier in self.players:
            logger.info('[GAME] Play {} from match <{}>'.format(identifier, self.identifier))
            self.players[identifier].play()
        