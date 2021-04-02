from src.asp.drawn import Drawn
from src.asp.row import Row
from src.asp.column import Column
from src.asp.step import Step
from src.core.game_match import GameMatch

from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram


class PlayerAgent:

    def __init__(self, id=None, match=None):
        self.id = id
        self.match = match
        self.row = Row(match.rows)
        self.column = Column(match.cols)
        try:
            self.handler = DesktopHandler(DLV2DesktopService('../../../lib/executable/dlv2win'))
            ASPMapper.get_instance().register_class(Drawn)
            ASPMapper.get_instance().register_class(Row)
            ASPMapper.get_instance().register_class(Column)
            ASPMapper.get_instance().register_class(Step)
        except Exception as e:
            print(str(e))

    def get_objects(self):
        objects = [self.row, self.column]
        orientation = ['v', 'h']

        for i in self.row.index:
            for j in self.column.index:
                for o in orientation:
                    if self.match.board[i][j][o] != 0:
                        objects.append(Drawn(i, j, o))

        return objects

    def play(self):
        input_program = ASPInputProgram()

        rules = open('agent.asp', 'r')

        input_program.add_objects_input(self.get_objects())
        input_program.add_program(rules)
        program_id = self.handler.add_program(input_program)
        answer_sets = self.handler.start_sync()

        sol = []
        for answerSet in answer_sets.get_optimal_answer_sets():
            for obj in answerSet.get_atoms():
                if isinstance(obj, Step):
                    sol.append(obj)

        self.handler.remove_program_from_id(program_id)
        return sol[0]
