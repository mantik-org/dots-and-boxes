from .agent import Agent

from ...asp.models.drawn import Drawn
from ...asp.models.row import Row
from ...asp.models.column import Column
from ...asp.models.chain import Chain

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
SOURCE = 'src/asp/chain.asp'

class ChainAgent(Agent):

    def __init__(self, player):
        Agent.__init__(self, [ 'src/asp/statement.asp', SOURCE ], [ '-n0' ])
        self.player = player
    

    def get_objects(self):
        return self.player.board_objects
    
    def play(self):
        try:
            return self.get_solution(self.get_answer_sets(), Chain)
        except Exception as e:
            logger.error(e)
            traceback.print_exc()
