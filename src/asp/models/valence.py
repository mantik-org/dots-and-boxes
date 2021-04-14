from lib.embasp.languages.predicate import Predicate


class Valence(Predicate):
    predicate_name = "valence"

    def __init__(self, row=None, column=None, value=None):
        Predicate.__init__(self, [("row", int), ("column", int), ("value", int)])
        self.row = row
        self.column = column
        self.value = value

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row

    def get_column(self):
        return self.column

    def set_column(self, column):
        self.column = column

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.column = value

    def __str__(self):
        return Valence.predicate_name + "(" + str(self.row) + "," + str(self.column) + str(self.value) + ")."
