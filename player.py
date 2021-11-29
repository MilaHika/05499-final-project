
class Player(object):
    name = "Player"
    def __init__(self, numplayers, id):
        self.history = []
        self.id = id
        self.reputation = [0] * numplayers
    
    def __repr__(self):
        return self.name

    def strategy(self, opponent):
        return None
    
    def play(self, opponent):
        s1, s2 = self.strategy(opponent), opponent.strategy(self)
        self.history.append(s1)
        opponent.history.append(s2)
        # print(s1, s2)
        if s1 == 'C':
            opponent.reputation[self.id] += 1
        else:
            opponent.reputation[self.id] -= 1
        if s2 == 'C':
            self.reputation[opponent.id] += 1
        else:
            self.reputation[opponent.id] -= 1
        return (s1, s2)
    
    def reset(self):
        self.history = []