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

class CurrentPhase(Predicate):
    predicate_name = "current_phase"

    def __init__(self, phase=None):
        Predicate.__init__(self, [("phase", int)])
        self.phase = phase

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def __str__(self):
        return CurrentPhase.predicate_name + "(" + str(self.phase) + ")."
