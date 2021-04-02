from src.asp.Drawn import Drawn
from src.asp.Row import Row
from src.asp.Column import Column
from src.asp.In import In

from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram


class PlayerAgent:

    def __init__(self, id=None, match=None):
        self.id = id
        self.row = Row(match.rows)
        self.column = Column(match.cols)
        try:
            self.handler = DesktopHandler(DLV2DesktopService('../../../lib/executable/dlv2win'))
            ASPMapper.get_instance().register_class(Drawn)
            ASPMapper.get_instance().register_class(Row)
            ASPMapper.get_instance().register_class(Column)
            ASPMapper.get_instance().register_class(In)
        except Exception as e:
            print(str(e))

    def get_objects(self):
        input = [self.row, self.column]
        return input

    def play(self):
        input_program = ASPInputProgram()

        rules = open('agent.asp', 'r')

        input_program.add_objects_input(self.get_objects())
        input_program.add_program(rules)
        program_id = self.handler.add_program(input_program)
        answer_sets = self.handler.start_sync()

        for answerSet in answer_sets.get_optimal_answer_sets():
            sol = []

            for obj in answerSet.get_atoms():

                if isinstance(obj, In):
                    sol.append(obj)

        self.handler.remove_program_from_id(program_id)
