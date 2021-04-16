#                                                                      
# GPL3 License 
#
# Author(s):                                                              
#      Antonino Natale <ntlnnn97r06e041t@studenti.unical.it>
#      Matteo Perfidio <prfmtt98e07f537p@studenti.unical.it>
# 
# 
# Copyright (C) 2021 AI Namp
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


    def add_player(self, identifier, socket):

        if not identifier in self.players:
            logger.info('[GAME] Registered new player {} in match <{}>'.format(identifier, self.identifier))
            self.players[identifier] = PlayerAgent(identifier, socket, self)
  


    def play(self, game, identifier):

        if identifier > MAX_PLAYERS:
            identifier = FIRST_PLAYER

        if identifier in self.players:

            next_move = self.players[identifier].play()
            self.board[next_move.row][next_move.column][next_move.orientation] = identifier

            logger.info('[GAME] Player {} drawn in {} from match <{}>'.format(identifier, next_move, self.identifier))

            game.update_match(self.identifier, identifier, [ next_move.row, next_move.column ], next_move.orientation, remote = True)





        