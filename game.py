

class Game():

    def __init__(self, r=3, s=0, t=5, p=1):
        self.scores = {
            ('C', 'C'): (r, r),
            ('D', 'D'): (p, p),
            ('C', 'D'): (s, t),
            ('D', 'C'): (t, s),
        }
    
    def score(self, pair):
        return self.scores[pair]