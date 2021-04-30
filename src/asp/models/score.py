#                                                                      
# GPL3 License 
#
# Author(s):                                                              
#      Antonino Natale <ntlnnn97r06e041t@studenti.unical.it>
#      Matteo Perfidio <prfmtt98e07f537p@studenti.unical.it>
# 
# 
# Copyright (C) 2021 Mantik
#
# This file is part of DotsAndBoxesAI.  
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

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
