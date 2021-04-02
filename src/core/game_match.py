
import logging
from ..ai.agent.player_agent import PlayerAgent

logger = logging.getLogger('debug')


MAX_PLAYERS  = 2
FIRST_PLAYER = 1

class GameMatch:

    def __init__(self, identifier, grid):

        rows, cols = grid

        self.identifier = identifier
        self.rows = rows
        self.cols = cols
        self.board = []
        self.score = []
        self.players = {}

        for _ in range(rows + 1):
            col = []
            for _ in range(cols + 1):
                col.append({ 'v' : 0, 'h': 0 })
            self.board.append(col)


    def add_player(self, identifier):

        if not identifier in self.players:
            logger.info('[GAME] Registered new player {} in match <{}>'.format(identifier, self.identifier))
            self.players[identifier] = PlayerAgent(identifier, self)
  


    def play(self, game, identifier):

        if identifier > MAX_PLAYERS:
            identifier = FIRST_PLAYER

        if identifier in self.players:

            next_move = self.players[identifier].play()
            self.board[next_move.row][next_move.column][next_move.orientation] = identifier

            logger.info('[GAME] Player {} drawn in {} from match <{}>'.format(identifier, next_move, self.identifier))

            game.update_match(self.identifier, identifier, [ next_move.row, next_move.column ], next_move.orientation, remote = True)





        