from lib.embasp.languages.predicate import Predicate
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant

class Debug(Predicate):
    predicate_name = "debug"

    def __init__(self, predicate=None):
        Predicate.__init__(self, [("predicate", SymbolicConstant)])
        self.predicate = predicate

    def get_predicate(self):
        return self.predicate

    def set_predicate(self, predicate):
        self.predicate = predicate

    def __str__(self):
        return Debug.predicate_name + "(" + str(self.predicate) + ")."
