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

import logging
import sys

from src.core.game import Game


def main(argv):

    logger = logging.getLogger('debug')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stderr))


    port = 8089
    
    if len(argv) > 1:
        port = argv[1]
    
    Game.getInstance().run('localhost', port)



if __name__ == '__main__':
    main(sys.argv)