
from tournament import *
from plot import *

if __name__ == '__main__':
    tournament = Tournament(numtrusts=50, numdistrusts=50, numcynicals=50, 
                            numliars=20, rounds=1000, trustprob=0.8, filepath='data8')
    tournament.playall()

    plotter = Plot(numtrusts=50, numdistrusts=50, numcynicals=50, 
                   numliars=20, rounds=1000, filepath='data8')
    plotter.reppayoff()
    plotter.payoffround()
    plotter.repround()
    plotter.histround()
    