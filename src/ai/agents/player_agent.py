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

from src.ai.agents.agent import Agent
from src.ai.agents.chain_agent import ChainAgent
from src.ai.agents.phase_agent import PhaseAgent

from src.asp.models.drawn import Drawn
from src.asp.models.row import Row
from src.asp.models.column import Column
from src.asp.models.step import Step
from src.asp.models.chain import Chain
from src.asp.models.cycle import Cycle
from src.asp.models.player import Player
from src.asp.models.phase import Phase
from src.asp.models.score import Score

from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant
from lib.embasp.base.option_descriptor import OptionDescriptor

import logging
import traceback
import platform
import time


logger = logging.getLogger('debug')
SOURCE = 'src/asp/player.asp'

class PlayerAgent(Agent):

    def __init__(self, id=None, socket=None, match=None):

        Agent.__init__(self, [ 'src/asp/utils.asp', SOURCE ], [], [ 'step/3' ])

        self.id = id
        self.match = match
        self.socket = socket
        self.chain = ChainAgent(self)
        self.phase = PhaseAgent(self)
        self.board_objects = []


    def get_objects(self):

        objects = []
        orientation = ['v', 'h']

    
        objects.append(Player(self.id))
        objects.append(Score(1, self.match.score[0]))
        objects.append(Score(2, self.match.score[1]))

        for i in range(self.match.rows + 1):
            objects.append(Row(i))
        
        for i in range(self.match.cols + 1):
            objects.append(Column(i))
            
        for i in range(self.match.rows + 1):
            for j in range(self.match.cols + 1):
                for o in orientation:
                    if self.match.board[i][j][o] != 0:
                        objects.append(Drawn(i, j, SymbolicConstant(o)))

        self.board_objects = objects


        i = 0
        answer_sets = self.chain.get_answer_sets()[0]

        for answer_set in answer_sets:
            i += 1
            for atom in answer_set.get_atoms():
                if isinstance(atom, Chain):
                    objects.append(Chain(i, atom.get_row(), atom.get_column()))
                elif isinstance(atom, Cycle):
                    objects.append(Cycle(i, atom.get_row(), atom.get_column()))

        self.phase_objects = objects


        objects.append(self.phase.play())

        return objects

    
    def prepare(self):
        return self.phase.play()
    
    def play(self):
        try:
            return self.get_solution(*self.get_answer_sets(), Step)[0]
        except Exception as e:
            logger.error(e)
            traceback.print_exc()
