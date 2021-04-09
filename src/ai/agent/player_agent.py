from .agent import Agent

from ...asp.drawn import Drawn
from ...asp.row import Row
from ...asp.column import Column
from ...asp.step import Step
from ...asp.phase import Phase

from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram
from lib.embasp.languages.asp.symbolic_constant import SymbolicConstant
from lib.embasp.base.option_descriptor import OptionDescriptor

import logging
import traceback
import platform

logger = logging.getLogger('debug')
SOURCE = 'src/asp/agent.asp'

class PlayerAgent(Agent):

    def __init__(self, id=None, socket=None, match=None):

        super.__init__([ SOURCE ], [])

        self.id = id
        self.match = match
        self.socket = socket

    
    def get_objects(self):

        objects = []
        orientation = ['v', 'h']


        for i in range(self.match.rows + 1):
            objects.append(Row(i))
        
        for i in range(self.match.cols + 1):
            objects.append(Column(i))
            
        for i in range(self.match.rows + 1):
            for j in range(self.match.cols + 1):
                for o in orientation:
                    if self.match.board[i][j][o] != 0:
                        objects.append(Drawn(i, j, SymbolicConstant(o)))
        
        for i in objects:
            logger.debug('[ASP] Generated object: {}'.format(i))

        return objects

    
    
    def play(self):
        try:
            return self.get_solution(self.get_answer_sets(), Step)
        except Exception as e:
            logger.error(e)
            traceback.print_exc()
