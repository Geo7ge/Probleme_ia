import time

from ProblemaRegineBKT import solve_queens
from ProblemaRegineAlpinist import configureRandomly, hillClimbing
from TravelingSalesman import travellingSalesmanProblem
from TravelingSalesmanAlpinist import readCoordinates, calcDistances, generateInitialTour, hillClimb
from ProblemaReginaCalireSimulata import simulated_annealing
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
            solving_times = []
            for i in range(len(table_sizes)):
                n = table_sizes[i]
                timp = time.time()
                time.sleep(1)
                solution = solve_queens(n)
                print(time.time() - timp - 1)
                solving_times.append(time.time() - timp - 1)
                # if solution:
                #     print(f"Soluție pentru problema reginelor cu {n} regine:")
                #     # print(solution)
                #     matrice = [["." for _ in range(n)] for i in range(n)]
                #     for i in solution:
                #         matrice[i][solution[i]] = "Q"
                #     for linie in matrice:
                #         print(linie)
                # else:
                #     print(f"Nu există soluție pentru problema reginelor cu {n} regine.")
            solving_times_alt = []
            for i in range(len(table_sizes)):
                n = table_sizes[i]
                timp = time.time()
                time.sleep(1)
                solution = solve_queens(n)
                print(time.time() - timp - 1)
                solving_times_alt.append(time.time() - timp - 1)
                # if solution:
                #     print(f"Soluție pentru problema reginelor cu {n} regine:")
                #     # print(solution)
                #     matrice = [["." for _ in range(n)] for i in range(n)]
                #     for i in solution:
                #         matrice[i][solution[i]] = "Q"
                #     for linie in matrice:
                #         print(linie)
                # else:
                #     print(f"Nu există soluție pentru problema reginelor cu {n} regine.")

        elif optiune == 2:
            solving_times = []
            for i in range(len(table_sizes)):
                n = table_sizes[i]
                state = [0] * n
                board = [[0 for i in range(n)] for j in range(n)]
                configureRandomly(board, state, n)
                timp = time.time()
                time.sleep(1)
                hillClimbing(board, state, n)
                print(time.time() - timp - 1)
                solving_times.append(time.time() - timp - 1)
                matrice = [["." for _ in range(n)] for i in range(n)]
            solving_times_alt = []
            for i in range(len(table_sizes)):
                n = table_sizes[i]
                state = [0] * n
                board = [[0 for i in range(n)] for j in range(n)]
                configureRandomly(board, state, n)
                timp = time.time()
                time.sleep(1)
                hillClimbing(board, state, n)
                print(time.time() - timp - 1)
                solving_times_alt.append(time.time() - timp - 1)
                matrice = [["." for _ in range(n)] for i in range(n)]

        elif optiune == 5:
            solving_times = []
            for i in range(len(table_sizes)):
                n = table_sizes[i]
                timp = time.time()
                time.sleep(1)
                simulated_annealing(n)
                print(time.time() - timp - 1)
                solving_times.append(time.time() - timp - 1)
            solving_times_alt = []
            for i in range(len(table_sizes)):
                n = table_sizes[i]
                timp = time.time()
                time.sleep(1)
                simulated_annealing(n)
                print(time.time() - timp - 1)
                solving_times_alt.append(time.time() - timp - 1)

        elif optiune == 6:
            solving_times = regine_algoritm_generic(table_sizes)
            solving_times_alt = regine_algoritm_generic(table_sizes)


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
