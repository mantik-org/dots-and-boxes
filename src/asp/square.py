from lib.embasp.languages.predicate import Predicate


class Square(Predicate):
    predicate_name = "square"

    def __init__(self, row=None, column=None):
        Predicate.__init__(self, [("row", int), ("column", int)])
        self.row = row
        self.column = column

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row

    def get_column(self):
        return self.column

    def set_column(self, column):
        self.column = column

    def __str__(self):
        return Square.predicate_name + "(" + str(self.row) + "," + str(self.column) + ")."
