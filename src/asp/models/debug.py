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
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant

class Debug(Predicate):
    predicate_name = "debug"

    def __init__(self, predicate=None, arg0=None, arg1=None, arg2=None):
        Predicate.__init__(self, [("predicate", SymbolicConstant), ("arg0", int), ("arg1", int), ("arg2", int)])
        self.predicate = predicate
        self.arg0 = arg0
        self.arg1 = arg1
        self.arg2 = arg2

    def get_predicate(self):
        return self.predicate

    def set_predicate(self, predicate):
        self.predicate = predicate

    def get_arg0(self):
        return self.arg0

    def set_arg0(self, arg0):
        self.arg0 = arg0

    def get_arg1(self):
        return self.arg1

    def set_arg1(self, arg1):
        self.arg1 = arg1

    def get_arg2(self):
        return self.arg2

    def set_arg2(self, arg2):
        self.arg2 = arg2

    def __str__(self):
        return Debug.predicate_name + "(" + str(self.predicate) + "," + str(self.arg0) + "," + str(self.arg1) + "," + str(self.arg2) + ")."
