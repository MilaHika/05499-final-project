from player import Player
from copy import deepcopy
from random import choices

class Trust(Player):
    name = 'Trust'

    def __init__(self, numplayers, id):
        super(Trust, self).__init__(numplayers, id)
    
    def strategy(self, opponent):
        opprep = self.reputation[opponent.id]
        self.reputation = deepcopy(opponent.reputation)
        self.reputation[opponent.id] = opprep
        if opprep == 0:
            coop = choices([0, 1], [0.5, 0.5])[0]
            return 'C' if coop else 'D'
        return 'C' if opprep > 0 else 'D'