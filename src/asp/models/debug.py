from lib.embasp.languages.predicate import Predicate
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant

class Debug(Predicate):
    predicate_name = "debug"

    def __init__(self, predicate=None, arg0=None, arg1=None):
        Predicate.__init__(self, [("predicate", SymbolicConstant), ("arg0", int), ("arg1", int)])
        self.predicate = predicate
        self.arg0 = arg0
        self.arg1 = arg1

    def get_predicate(self):
        return self.predicate

    def set_predicate(self, predicate):
        self.predicate = predicate

    def get_arg0(self):
        return self.arg0

    def set_arg0(self, arg0):
        self.arg0 = arg0

    def get_arg1(self):
        return self.arg1

    def set_arg1(self, arg1):
        self.arg1 = arg1

    def __str__(self):
        return Debug.predicate_name + "(" + str(self.predicate) + "," + str(self.arg0) + "," + str(self.arg1) + ")."
