#                                                                      
# GPL3 License 
#
# Author(s):                                                              
#      Antonino Natale <ntlnnn97r06e041t@studenti.unical.it>
#      Matteo Perfidio <prfmtt98e07f537p@studenti.unical.it>
# 
# 
# Copyright (C) 2021 AI Namp
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
