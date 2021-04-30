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
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant

class Drawn(Predicate):
    predicate_name = "drawn"

    def __init__(self, row=None, column=None, orientation=None):
        Predicate.__init__(self, [("row", int), ("column", int), ("orientation", SymbolicConstant)])
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
        return Drawn.predicate_name + "(" + str(self.row) + "," + str(self.column) + "," + str(self.orientation) + ")."
