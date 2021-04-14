from lib.embasp.languages.predicate import Predicate


class Cycle(Predicate):
    predicate_name = "cycle"

    def __init__(self, identifier=None, row=None, column=None):
        Predicate.__init__(self, [("identifier", int), ("row", int), ("column", int)])
        self.row = row
        self.column = column
        self.identifier = identifier

    def get_identifier(self):
        return self.identifier
    
    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row

    def get_column(self):
        return self.column

    def set_column(self, column):
        self.column = column

    def __str__(self):
        return Cycle.predicate_name + "(" + str(self.identifier) + "," + str(self.row) + "," + str(self.column) + ")."
