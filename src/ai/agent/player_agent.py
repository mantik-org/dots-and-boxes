from ...asp.drawn import Drawn
from ...asp.row import Row
from ...asp.column import Column
from ...asp.step import Step

from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant

import logging
import traceback

logger = logging.getLogger('debug')
SOURCE = 'src/asp/agent.asp'

class PlayerAgent:

    def __init__(self, id=None, match=None):

        self.id = id
        self.match = match

        logger.info('[ASP] Reading source code from {}'.format(SOURCE))

        with open(SOURCE, 'r') as rules:
            self.source = rules.read()


        try:

            self.handler = DesktopHandler(DLV2DesktopService('lib/executable/dlv2linux'))
            ASPMapper.get_instance().register_class(Drawn)
            ASPMapper.get_instance().register_class(Row)
            ASPMapper.get_instance().register_class(Column)
            ASPMapper.get_instance().register_class(Step)

        except Exception as e:
            print(str(e))


    def get_objects(self):

        objects = []
        orientation = ['v', 'h']


        for i in range(self.match.rows + 1):
            objects.append(Row(i))
        
        for i in range(self.match.cols + 1):
            objects.append(Column(i))
            
        for i in range(self.match.rows + 1):
            for j in range(self.match.cols + 1):
                for o in orientation:
                    if self.match.board[i][j][o] != 0:
                        objects.append(Drawn(i, j, SymbolicConstant(o)))
        
        for i in objects:
            logger.debug('[ASP] Generated object: {}'.format(i))

        return objects


    def play(self):


        input_program = ASPInputProgram()

        logger.info("[ASP] Reading source file")

        try:
            
            input_program.add_objects_input(self.get_objects())
            input_program.add_program(self.source)

            program_id = self.handler.add_program(input_program)
            answer_sets = self.handler.start_sync()

            logger.info("[ASP] Getting solution from {}".format(program_id))

            if 'OPTIMUM' in answer_sets.get_answer_sets_string():
                answer_sets = answer_sets.get_optimal_answer_sets()
            else:
                answer_sets = answer_sets.get_answer_sets()

            sol = []
            for answer_set in answer_sets:
                for obj in answer_set.get_atoms():
                    if isinstance(obj, Step):
                        sol.append(obj)

            self.handler.remove_program_from_id(program_id)


            if len(sol) > 0:
                return sol[0]

            raise Exception('[ASP] No solution found')

        except Exception as e:
            logger.error(e)
            traceback.print_exc()
