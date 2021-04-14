from lib.embasp.languages.predicate import Predicate


class Phase(Predicate):
    predicate_name = "phase"

    def __init__(self, phase=None):
        Predicate.__init__(self, [("phase", int)])
        self.phase = phase

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def __str__(self):
        return Phase.predicate_name + "(" + str(self.phase) + ")."
