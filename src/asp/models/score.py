from lib.embasp.languages.predicate import Predicate

class Score(Predicate):
    predicate_name = "score"

    def __init__(self, player=None, points=None):
        Predicate.__init__(self, [("player", int), ("points", int)])
        self.player = player
        self.points = points

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def __str__(self):
        return Score.predicate_name + "(" + str(self.player) + "," + str(self.points) + ")."
