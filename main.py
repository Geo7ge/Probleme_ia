import time

from ProblemaRegineBKT import solve_queens, ProblemaRegineBkt
from ProblemaRegineAlpinist import configureRandomly, hillClimbing, ProblemaRegineAlp
from TravelingSalesman import travellingSalesmanProblem
from TravelingSalesmanAlpinist import readCoordinates, calcDistances, generateInitialTour, hillClimb
from ProblemaReginaCalireSimulata import simulated_annealing, ProblemaRegineCS
from ProblemaRegineAlgoritmGenetic import regine_algoritm_generic
from plot import plot_chart



if __name__ == "__main__":
    table_sizes =[8, 12, 16, 20, 22]
    solving_times = []
    solving_times_alt = []
    print("1 - problema regine bkt")
    print("2 - problema regine alpinist")
    print("5 - problema regine calire simulata")
    print("6 - problema regine algoritm generic")
    print("3 - problema comis voiajorului")
    print("4 - problema comis voiajorului alpinist")
    print("10 - grafic problema N regine")
    print("0- EXIT")
    while(True):
        optiune = int(input("Introduceti optiunea aleasa: "))
        if optiune == 1:
            solving_times_alt = solving_times
            solving_times = ProblemaRegineBkt(table_sizes)

        elif optiune == 2:
            solving_times_alt = solving_times
            solving_times = ProblemaRegineAlp(table_sizes)

        elif optiune == 5:
            solving_times_alt = solving_times
            solving_times = ProblemaRegineCS(table_sizes)

        elif optiune == 6:
            solving_times_alt = solving_times
            solving_times = regine_algoritm_generic(table_sizes)

        elif optiune == 3:
            graph = [[0, 10, 15, 20], [10, 0, 35, 20], [15, 35, 0, 30], [50, 65, 30, 0]]
            s = 0
            print(travellingSalesmanProblem(graph, s))

        elif optiune == 4:
            cityCoordinates = readCoordinates("intput2.txt")
            distances = calcDistances(cityCoordinates)
            numberOfCities = len(cityCoordinates)
            initialTour = generateInitialTour(numberOfCities)
            numberOfRepetitions = input("Enter number of repetitions")
            finalTour, finalValue, repetitions = hillClimb(numberOfCities, numberOfRepetitions, distances)
            print("The best tour is: ")
            print(finalTour)

        elif optiune == 10:
            plot_chart(table_sizes, solving_times, solving_times_alt)
            pass
        elif optiune == 0:
            break
