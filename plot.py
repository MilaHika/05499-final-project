import json
import matplotlib.pyplot as plt

class Plot():
    def __init__(self, numtrusts=50, numdistrusts=50, numcynicals=50, 
                 numliars=20, rounds=1000, filepath='data'):
        self.filepath = filepath
        jsonFile = open(filepath+'/data.json')
        jsonFile = json.load(jsonFile)
        self.data = jsonFile['data']
        self.history = jsonFile['history']
        self.numtrusts = numtrusts
        self.numdistrusts = numdistrusts
        self.numcynicals = numcynicals
        self.numliars = numliars
        self.rounds = rounds

    def reppayoff(self):
        lastround = self.data[-1]
        roundid = len(self.data)-1
        
        trustsx = lastround['payoff'][0:self.numtrusts]
        trustsy = lastround['reputation'][0:self.numtrusts]
        distrustx = lastround['payoff'][self.numtrusts:self.numtrusts+self.numdistrusts]
        distrusty = lastround['reputation'][self.numtrusts:self.numtrusts+self.numdistrusts]
        cynicalx = lastround['payoff'][self.numtrusts+self.numdistrusts:self.numtrusts+self.numdistrusts+self.numcynicals]
        cynicaly = lastround['reputation'][self.numtrusts+self.numdistrusts:self.numtrusts+self.numdistrusts+self.numcynicals]
        liarsx = lastround['payoff'][-self.numliars:]
        liarsy = lastround['reputation'][-self.numliars:]

        plt.scatter(trustsx, trustsy, label='Trust', color='green')
        plt.scatter(distrustx, distrusty, label='Distrust', color='red')
        if self.numcynicals:
            plt.scatter(cynicalx, cynicaly, label='Cynical', color='blue')
        if self.numliars:
            plt.scatter(liarsx, liarsy, label='Liar', color='gray')

        plt.xlabel('Payoff')
        plt.ylabel('Reputation')
        plt.title(f'Reputation vs. Payoff Round {roundid+1}')
        plt.legend(loc='upper left')
        plt.savefig(self.filepath + '/reppayoff.png')
        plt.close()
    
    def payoffround(self):
        trusty = []
        distrusty = []
        cynicaly = []
        liarsy = []
        
        for roundi in self.data:
            trustavg = sum(roundi['payoff'][0:self.numtrusts])/self.numtrusts
            trusty.append(trustavg)
            distrustavg = roundi['payoff'][self.numtrusts:self.numtrusts+self.numdistrusts]
            distrustavg = sum(distrustavg)/self.numdistrusts
            distrusty.append(distrustavg)
            if self.numcynicals:
                cynicalavg = sum(roundi['payoff'][self.numtrusts+self.numdistrusts:self.numtrusts+self.numdistrusts+self.numcynicals])/self.numcynicals
                cynicaly.append(cynicalavg)
            if self.numliars:
                liarsavg = sum(roundi['payoff'][-self.numliars:])/self.numliars
                liarsy.append(liarsavg)
        
        roundx = [i+1 for i in range(self.rounds)]
        
        plt.plot(roundx, trusty, label='Trust')
        plt.plot(roundx, distrusty, label='Distrust')
        if self.numcynicals:
            plt.plot(roundx, cynicaly, label='Cynical')
        if self.numliars:
            plt.plot(roundx, liarsy, label='Liars')

        plt.xlabel('Round')
        plt.ylabel('Payoff')
        plt.title('Payoff vs. Round')
        plt.legend(loc='upper left')
        plt.savefig(self.filepath + '/payoffround.png')
        plt.close()
    
    def repround(self):
        trusty = []
        distrusty = []
        cynicaly = []
        liarsy = []
        
        for roundi in self.data:
            trustavg = sum(roundi['reputation'][0:self.numtrusts])/self.numtrusts
            trusty.append(trustavg)
            distrustavg = roundi['reputation'][self.numtrusts:self.numtrusts+self.numdistrusts]
            distrustavg = sum(distrustavg)/self.numdistrusts
            distrusty.append(distrustavg)
            if self.numcynicals:
                cynicalavg = sum(roundi['reputation'][self.numtrusts+self.numdistrusts:self.numtrusts+self.numdistrusts+self.numcynicals])/self.numcynicals
                cynicaly.append(cynicalavg)
            if self.numliars:
                liarsavg = sum(roundi['reputation'][-self.numliars:])/self.numliars
                liarsy.append(liarsavg)
        
        roundx = [i+1 for i in range(self.rounds)]
        
        plt.plot(roundx, trusty, label='Trust')
        plt.plot(roundx, distrusty, label='Distrust')
        if self.numcynicals:
            plt.plot(roundx, cynicaly, label='Cynical')
        if self.numliars:
            plt.plot(roundx, liarsy, label='Liars')

        plt.xlabel('Round')
        plt.ylabel('Reputation')
        plt.title('Reputation vs. Round')
        plt.legend(loc='upper left')
        plt.savefig(self.filepath + '/repround.png')
        plt.close()
    
    def histround(self):
        trusty = []
        distrusty = []
        cynicaly = []
        liary = []
        
        for roundi in range(self.rounds):
            trustc = 0
            distrustc = 0
            cynicalc = 0
            liarc = 0

            for i, player in enumerate(self.history):
                if i < self.numtrusts and player[roundi] == 'C':
                    trustc += 1
                elif i < self.numtrusts+self.numdistrusts and player[roundi] == 'C':
                    distrustc += 1
                elif i < self.numtrusts+self.numdistrusts+self.numcynicals \
                    and player[roundi] == 'C':
                    cynicalc += 1
                elif i < self.numtrusts+self.numdistrusts+self.numcynicals+self.numliars \
                    and player[roundi] == 'C':
                    liarc += 1

            trusty.append(trustc)
            distrusty.append(distrustc)
            cynicaly.append(cynicalc)
            liary.append(liarc)

        roundx = [i+1 for i in range(self.rounds)]

        plt.plot(roundx, trusty, label='Trust')
        plt.plot(roundx, distrusty, label='Distrust')
        if self.numcynicals:
            plt.plot(roundx, cynicaly, label='Cynical')
        if self.numliars:
            plt.plot(roundx, liary, label='Liar')

        plt.xlabel('Round')
        plt.ylabel('Cooperation')
        plt.title('Cooperation vs. Round')
        plt.legend(loc='upper left')
        plt.savefig(self.filepath + '/coopround.png')
        plt.close()

        trusty = [self.numtrusts-i for i in trusty]
        distrusty = [self.numdistrusts-i for i in distrusty]
        cynicaly = [self.numcynicals-i for i in cynicaly]
        liary = [self.numliars-i for i in liary]
        
        plt.plot(roundx, trusty, label='Trust')
        plt.plot(roundx, distrusty, label='Distrust')
        if self.numcynicals:
            plt.plot(roundx, cynicaly, label='Cynical')
        if self.numliars:
            plt.plot(roundx, liary, label='Liar')

        plt.xlabel('Round')
        plt.ylabel('Defect')
        plt.title('Defect vs. Round')
        plt.legend(loc='upper left')
        plt.savefig(self.filepath + '/defectround.png')
        plt.close()


if __name__ == '__main__':
    plotter = Plot()
    plotter.reppayoff()
    plotter.payoffround()
    plotter.repround()
    plotter.histround()
