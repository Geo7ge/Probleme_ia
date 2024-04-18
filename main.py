import time

from ProblemaRegineBKT import solve_queens
from ProblemaRegineAlpinist import configureRandomly, hillClimbing
from TravelingSalesman import travellingSalesmanProblem
from TravelingSalesmanAlpinist import readCoordinates, calcDistances, generateInitialTour, hillClimb

if __name__ == "__main__":
    print("1 - problema regine bkt")
    print("2 - problema regine alpinist")
    print("3 - problema comis voiajorului")
    print("3 - problema comis voiajorului alpinist")
    optiune = int(input("Introduceti optiunea aleasa: "))
    if optiune == 1:
        n = int(input("Introduceti dimensiunea tablei de sah: "))
        timp = time.time()
        time.sleep(1)
        solution = solve_queens(n)
        print(time.time() - timp - 1)

        if solution:
            print(f"Soluție pentru problema reginelor cu {n} regine:")
            # print(solution)
            matrice = [["." for _ in range(n)] for i in range(n)]
            for i in solution:
                matrice[i][solution[i]] = "Q"
            for linie in matrice:
                print(linie)
        else:
            print(f"Nu există soluție pentru problema reginelor cu {n} regine.")

    elif optiune == 2:
        n = int(input("Introduceti dimensiunea tablei de sah"))
        state = [0] * n
        board = [[0 for _ in range(n)] for _ in range(n)]

        configureRandomly(board, state)

        hillClimbing(board, state)
        matrice = [["." for _ in range(n)] for i in range(n)]

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