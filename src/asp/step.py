from lib.embasp.languages.predicate import Predicate


class Step(Predicate):
    predicate_name = "step"

    def __init__(self, row=None, column=None, orientation=None):
        Predicate.__init__(self, ["row", "column", "orientation"])
        self.row = row
        self.column = column
        self.orientation = orientation

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_orientation(self):
        return self.orientation

    def set_row(self, row):
        self.row = row

    def set_column(self, column):
        self.column = column

    def set_orientation(self, orientation):
        self.orientation = orientation

    def __str__(self):
        return Step.predicate_name + "(" + str(self.row) + "," + str(self.column) + "," + str(self.orientation) + ")."
