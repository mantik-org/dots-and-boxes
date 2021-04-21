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

from src.ai.agents.agent import Agent

from src.asp.models.drawn import Drawn
from src.asp.models.row import Row
from src.asp.models.column import Column
from src.asp.models.chain import Chain
from src.asp.models.phase import Phase
from src.asp.models.current_phase import CurrentPhase

from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant
from lib.embasp.base.option_descriptor import OptionDescriptor

import logging
import traceback
import platform

logger = logging.getLogger('debug')
SOURCE = 'src/asp/phase.asp'

class PhaseAgent(Agent):

    def __init__(self, player):
        Agent.__init__(self, [ 'src/asp/utils.asp', SOURCE ], [], [ 'current_phase/1', 'phase/1' ])
        self.player = player
        self.phase = 1
    

    def get_objects(self):
        objects = self.player.phase_objects
        objects.append(CurrentPhase(self.phase))
        return objects
    
    def play(self):
        try:

            phase_object = self.get_solution(*self.get_answer_sets(), Phase)[0]

            self.phase = phase_object.get_phase()
            return phase_object

        except Exception as e:
            logger.error(e)
            traceback.print_exc()
