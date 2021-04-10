from ...asp.drawn import Drawn
from ...asp.row import Row
from ...asp.column import Column
from ...asp.step import Step
from ...asp.phase import Phase
from ...asp.chain import Chain
from ...asp.valence import Valence
from ...asp.grid import Grid
from ...asp.square import Square

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
        ASPMapper.get_instance().register_class(Drawn)
        ASPMapper.get_instance().register_class(Row)
        ASPMapper.get_instance().register_class(Column)
        ASPMapper.get_instance().register_class(Step)
        ASPMapper.get_instance().register_class(Phase)
        ASPMapper.get_instance().register_class(Chain)
        ASPMapper.get_instance().register_class(Valence)
        ASPMapper.get_instance().register_class(Grid)
        ASPMapper.get_instance().register_class(Square)

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

        if len(sol) == 0:
            raise Exception('[ASP] No solution found')

        return sol[0]


    def play(self):
        pass