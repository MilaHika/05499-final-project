from game import *
from trust import *
from distrust import *
from cynical import *
from liar import *

import os
import json
from copy import deepcopy
from random import randrange

class Tournament():

    def __init__(self, numtrusts=50, numdistrusts=50, numcynicals=50, 
                 numliars=20, rounds=1000, trustprob=0.8, filepath='data'):
        self.log = []
        self.currround = 0
        self.filepath = filepath

        self.rounds = rounds
        self.game = Game()
        self.numplayers = numtrusts+numdistrusts+numcynicals+numliars
        self.payoffs = [0] * self.numplayers
        self.players = []
        for i in range(self.numplayers):
            if i  < numtrusts:
                self.players.append(Trust(self.numplayers, i))
            elif i < numtrusts+numdistrusts:
                self.players.append(Distrust(self.numplayers, i, trustprob))
            elif i < numtrusts+numdistrusts+numcynicals:
                self.players.append(Cynical(self.numplayers, i))
            else:
                self.players.append(Liar(self.numplayers, i))
        # print(self.players)

    def matches(self):
        unmatched = [i for i in range(self.numplayers)]
        pairs = []
        while len(unmatched) > 0:
            rand1 = unmatched.pop(randrange(0, len(unmatched)))
            rand2 = unmatched.pop(randrange(0, len(unmatched)))
            pairs.append((rand1, rand2))
        return pairs
    
    def play1round(self):
        matched = self.matches()
        for match in matched:
            # print(f'Match: {match}')
            p1, p2 = match
            player1, player2 = self.players[p1], self.players[p2]
            pair = player1.play(player2)
            self.payoffs[p1] += self.game.score(pair)[0]
            self.payoffs[p2] += self.game.score(pair)[1]
    
    def reputation(self):
        reps = [0] * self.numplayers

        for player in self.players:
            # print(f'Player: {player.id}|{player} Reputation: {player.reputation}')
            reps = [x+y for (x,y) in zip(reps, player.reputation)]
        reps = [rep/self.numplayers for rep in reps]
        return reps
    
    def history(self):
        hist = []
        for player in self.players:
            hist.append(player.history)
        return hist

    def playall(self, log=True):
        for i in range(self.rounds):
            data = {}
            data['payoff'] = deepcopy(self.payoffs)
            data['reputation'] = self.reputation()
            self.log.append(data)
            self.play1round()
            self.currround += 1

        if log:
            alldata = {}
            alldata['history'] = self.history()
            alldata['data'] = self.log

            # print(self.payoffs)
            # print(self.reputation())
            if not os.path.exists(self.filepath):
                os.makedirs(self.filepath)
            jsonString = json.dumps(alldata)
            jsonFile = open(self.filepath+'/data.json', 'w')
            jsonFile.write(jsonString)
            jsonFile.close()
    
        
        