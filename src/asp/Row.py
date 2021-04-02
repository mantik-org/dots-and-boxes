from lib.embasp.languages.predicate import Predicate


class Row(Predicate):
    predicate_name = "Row"

    def __init__(self, index=None):
        Predicate.__init__(self, ["index"])
        self.index = index

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def __str__(self):
        return Row.predicate_name + "(" + str(self.index) + ")."
