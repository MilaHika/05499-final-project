
from tournament import *
from plot import *

if __name__ == '__main__':
    tournament = Tournament(numtrusts=50, numdistrusts=150, numcynicals=0, 
                            numliars=0, rounds=1000, trustprob=0.2, filepath='data7')
    tournament.playall()

    plotter = Plot(numtrusts=50, numdistrusts=150, numcynicals=0, 
                   numliars=0, rounds=1000, filepath='data7')
    plotter.reppayoff()
    plotter.payoffround()
    plotter.repround()
    plotter.histround()
    