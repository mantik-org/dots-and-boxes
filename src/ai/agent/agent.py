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

from ...asp.models.debug import Debug
from ...asp.models.drawn import Drawn
from ...asp.models.row import Row
from ...asp.models.column import Column
from ...asp.models.step import Step
from ...asp.models.phase import Phase
from ...asp.models.chain import Chain
from ...asp.models.cycle import Cycle
from ...asp.models.valence import Valence
from ...asp.models.grid import Grid
from ...asp.models.square import Square
from ...asp.models.player import Player

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


class Agent:

    @staticmethod
    def initMappings():
        logger.info('[ASP] Registering object mapping')
        ASPMapper.get_instance().register_class(Debug)
        ASPMapper.get_instance().register_class(Drawn)
        ASPMapper.get_instance().register_class(Row)
        ASPMapper.get_instance().register_class(Column)
        ASPMapper.get_instance().register_class(Step)
        ASPMapper.get_instance().register_class(Phase)
        ASPMapper.get_instance().register_class(Chain)
        ASPMapper.get_instance().register_class(Cycle)
        ASPMapper.get_instance().register_class(Valence)
        ASPMapper.get_instance().register_class(Grid)
        ASPMapper.get_instance().register_class(Square)
        ASPMapper.get_instance().register_class(Player)

    def __init__(self, sources, options):

        self.sources = []

        for source in sources:
            logger.info('[ASP] Reading source code from {}'.format(source))
            with open(source, 'r') as rules:
                self.sources.append(rules.read())


        try:

            if platform.system() == 'Linux':
                self.handler = DesktopHandler(DLV2DesktopService('lib/executable/dlv2linux'))
            elif platform.system() == 'Windows':
                self.handler = DesktopHandler(DLV2DesktopService('lib/executable/dlv2win'))
            elif platform.system() == 'Darwin':
                self.handler = DesktopHandler(DLV2DesktopService('lib/executable/dlv2.mac_7'))
            else:
                raise Exception('[ASP] Unsupported operating system')

            for option in options:
                self.handler.add_option(OptionDescriptor(option))

        except Exception as e:
            print(str(e))

    
    def get_objects(self):
        pass

    def get_answer_sets(self):

        input_program = ASPInputProgram()
        input_program.add_objects_input(self.get_objects())

        for source in self.sources:
            input_program.add_program(source)


        program_id = self.handler.add_program(input_program)
        answer_sets = self.handler.start_sync()
        self.handler.remove_program_from_id(program_id)


        #logger.debug('[ASP] Got answer sets: {}'.format(answer_sets.get_answer_sets_string()))

        if 'OPTIMUM' in answer_sets.get_answer_sets_string():
            answer_sets = answer_sets.get_optimal_answer_sets()
        else:
            answer_sets = answer_sets.get_answer_sets()

        return answer_sets



    def get_solution(self, answer_sets, solution):

        if len(answer_sets) == 0:
            raise Exception('[ASP] No answer set found')

        sol = []
        answer_set = answer_sets[0]

        for obj in answer_set.get_atoms():
            if isinstance(obj, solution):
                sol.append(obj)
            elif isinstance(obj, Debug):
                logger.info('[DEBUG] Activated {}'.format(str(obj)))

        if len(sol) == 0:
            raise Exception('[ASP] No solution found')

        return sol[0]


    def play(self):
        pass