from lib.embasp.languages.predicate import Predicate


class Column(Predicate):
    predicate_name = "cols"

    def __init__(self, index=None):
        Predicate.__init__(self, [("index", int)])
        self.index = index

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def __str__(self):
        return Column.predicate_name + "(" + str(self.index) + ")."
