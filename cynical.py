from player import Player
from copy import deepcopy
from random import choices

class Cynical(Player):
    name = 'Cynical'

    def __init__(self, numplayers, id):
        super(Cynical, self).__init__(numplayers, id)
    
    def strategy(self, opponent):
        opprep = self.reputation[opponent.id]
        if opprep == 0:
            coop = choices([0, 1], [0.5, 0.5])[0]
            return 'C' if coop else 'D'
        return 'C' if opprep > 0 else 'D'