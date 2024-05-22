import time

from Graphics import showGraph
from ProblemaRegineBKT import solve_queens, ProblemaRegineBkt
from ProblemaRegineAlpinist import configureRandomly, hillClimbing, ProblemaRegineAlp
from TravelingSalesman import travellingSalesmanProblem, travellingSalesman
from TravelingSalesmanAlpinist import readCoordinates, calcDistances, generateInitialTour, hillClimb, \
    travelingSalesmanAplinist
from ProblemaReginaCalireSimulata import simulated_annealing, ProblemaRegineCS
from ProblemaRegineAlgoritmGenetic import regine_algoritm_generic
from plot import plot_chart


if __name__ == "__main__":
    table_sizes = [8, 12, 16, 20, 22]
    solving_times = []
    solving_times_alt = []
    print("1 - problema regine bkt")
    print("2 - problema regine alpinist")
    print("3 - problema regine calire simulata")
    print("4 - problema regine algoritm generic")
    print("5 - problema comis voiajorului")
    print("6 - problema comis voiajorului alpinist")
    print("10 - grafic problema N regine")
    print("11 - grafic pentru problema reginelor folosind date deja existente")
    print("0- EXIT")
    while(True):
        optiune = int(input("Introduceti optiunea aleasa: "))
        if optiune == 1:
            solving_times_alt = solving_times
            solving_times = ProblemaRegineBkt(table_sizes)

        elif optiune == 2:
            solving_times_alt = solving_times
            solving_times = ProblemaRegineAlp(table_sizes)

        elif optiune == 3:
            solving_times_alt = solving_times
            solving_times = ProblemaRegineCS(table_sizes)

        elif optiune == 4:
            solving_times_alt = solving_times
            solving_times = regine_algoritm_generic(table_sizes)

        elif optiune == 5:
            travellingSalesman()

        elif optiune == 6:
            travelingSalesmanAplinist()

        elif optiune == 10:
            plot_chart(table_sizes, solving_times, solving_times_alt)

        elif optiune == 11:
            showGraph()
            pass
        elif optiune == 0:
            break
