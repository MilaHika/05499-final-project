from player import Player
from copy import deepcopy
from random import choices

class Liar(Player):
    name = 'Liar'

    def __init__(self, numplayers, id):
        super(Liar, self).__init__(numplayers, id)
    
    def strategy(self, opponent):
        opprep = self.reputation[opponent.id]
        opponent.reputation = [-100000]*len(self.reputation)
        if opprep == 0:
            coop = choices([0, 1], [0.5, 0.5])[0]
            return 'C' if coop else 'D'
        return 'C' if opprep > 0 else 'D'