from .agent import Agent
from.chain_agent import ChainAgent

from ...asp.models.drawn import Drawn
from ...asp.models.row import Row
from ...asp.models.column import Column
from ...asp.models.step import Step
from ...asp.models.chain import Chain
from ...asp.models.cycle import Cycle

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
SOURCE = 'src/asp/phases.asp'

class PlayerAgent(Agent):

    def __init__(self, id=None, socket=None, match=None):

        Agent.__init__(self, [ 'src/asp/statement.asp', SOURCE ], [])

        self.id = id
        self.match = match
        self.socket = socket
        self.chain = ChainAgent(self)
        self.board_objects = []


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

        self.board_objects = objects


        i = 0
        chains = 0
        cycles = 0
        answer_sets = self.chain.get_answer_sets()

        for answer_set in answer_sets:
            i += 1
            for atom in answer_set.get_atoms():
                if isinstance(atom, Chain):
                    objects.append(Chain(i, atom.get_row(), atom.get_column()))
                    chains += 1
                elif isinstance(atom, Cycle):
                    objects.append(Cycle(i, atom.get_row(), atom.get_column()))
                    cycles += 1
        logger.info('Chains / Cycles {} {}'.format(chains, cycles))

        return objects

    
    
    def play(self):
        try:

            return self.get_solution(self.get_answer_sets(), Step)

        except Exception as e:
            logger.error(e)
            traceback.print_exc()
