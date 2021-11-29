from player import Player
from copy import deepcopy
from random import choices

class Liar(Player):
    name = 'Liar'

    def __init__(self, numplayers, id):
        super(Liar, self).__init__(numplayers, id)
        self.reputation = [-100000]*len(self.reputation)
        self.realreputation = [0] * numplayers
    
    def strategy(self, opponent):
        opprep = self.realreputation[opponent.id]
        myrep = opponent.reputation[self.id]
        opponent.reputation = self.reputation
        opponent.reputation[self.id] = myrep
        if opprep == 0:
            coop = choices([0, 1], [0.5, 0.5])[0]
            return 'C' if coop else 'D'
        return 'C' if opprep > 0 else 'D'