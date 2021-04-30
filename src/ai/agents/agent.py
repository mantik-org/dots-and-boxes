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

from src.asp.models.drawn import Drawn
from src.asp.models.row import Row
from src.asp.models.column import Column
from src.asp.models.step import Step
from src.asp.models.phase import Phase
from src.asp.models.chain import Chain
from src.asp.models.cycle import Cycle
from src.asp.models.score import Score
from src.asp.models.player import Player
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
import random
import time

logger = logging.getLogger('debug')
filters = []

class Agent:

    @staticmethod
    def initMappings():

        logger.info('[ASP] Registering object mapping')
        ASPMapper.get_instance().register_class(Drawn)
        ASPMapper.get_instance().register_class(Row)
        ASPMapper.get_instance().register_class(Column)
        ASPMapper.get_instance().register_class(Step)
        ASPMapper.get_instance().register_class(Phase)
        ASPMapper.get_instance().register_class(Chain)
        ASPMapper.get_instance().register_class(Cycle)
        ASPMapper.get_instance().register_class(Score)
        ASPMapper.get_instance().register_class(Player)
        ASPMapper.get_instance().register_class(CurrentPhase)

        logger.info('[ASP] Registering filters')
        filters.append('drawn/3')
        filters.append('rows/1')
        filters.append('cols/1')
        filters.append('step/3')
        filters.append('phase/1')
        filters.append('chain/3')
        filters.append('cycle/3')
        filters.append('score/2')
        filters.append('player/1')
        filters.append('current_phase/1')




    def __init__(self, sources, options, dependencies=[]):

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


            if len(dependencies) == 0:
                dependencies = filters

            options.append('--filter={}'.format(','.join(dependencies)))


            for option in options:
                self.handler.add_option(OptionDescriptor(option))

        except Exception as e:
            logger.error(str(e))

    
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


        start = time.time()
        optimum = False

        if 'OPTIMUM' in answer_sets.get_answer_sets_string():
            answer_sets = answer_sets.get_optimal_answer_sets()
            optimum = True
        else:
            answer_sets = answer_sets.get_answer_sets()

        end = time.time()

        logger.info("[BENCH] Running {} in {}s".format(self.__class__.__name__, (end - start)))

        return ( answer_sets, optimum )



    def get_solution(self, answer_sets, optimum , solution, *args):

        if len(answer_sets) == 0:
            raise Exception('[ASP] No answer set found')


        sol = []
        opt = []

        if optimum:
            answer_sets = answer_sets[0:1]

        for answer_set in answer_sets:
            for obj in answer_set.get_atoms():
                if isinstance(obj, solution):
                    sol.append(obj)
                else:
                    for arg in args:
                        if isinstance(obj, arg):
                            opt.append(obj)


        if len(sol) == 0:
            raise Exception('[ASP] No solution found')


        preferred = sol[0]

        if not optimum:
            preferred = random.choice(sol)

        return ( preferred, opt )


    def play(self):
        pass