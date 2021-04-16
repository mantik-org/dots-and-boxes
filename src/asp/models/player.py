from lib.embasp.languages.predicate import Predicate


class Player(Predicate):
    predicate_name = "player"

    def __init__(self, index=None):
        Predicate.__init__(self, [("index", int)])
        self.index = index

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def __str__(self):
        return Player.predicate_name + "(" + str(self.index) + ")."
