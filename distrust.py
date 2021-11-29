from player import Player
from copy import deepcopy
from random import choices

class Distrust(Player):
    name = 'Distrust'

    def __init__(self, numplayers, id, trustprob):
        super(Distrust, self).__init__(numplayers, id)
        self.trustprob = [1-trustprob, trustprob]

    def strategy(self, opponent):
        trust = choices([0, 1], self.trustprob)[0]
        opprep = self.reputation[opponent.id]
        if trust:
            opprep = self.reputation[opponent.id]
            self.reputation = deepcopy(opponent.reputation)
            self.reputation[opponent.id] = opprep

        if opprep == 0:
            coop = choices([0, 1], [0.5, 0.5])[0]
            return 'C' if coop else 'D'
        return 'C' if opprep > 0 else 'D'
