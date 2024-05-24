import sys
from random import shuffle
from math import *

def travelingSalesmanAplinist():
    cityCoordinates = readCoordinates("intput2.txt")
    distances = calcDistances(cityCoordinates)
    numberOfCities = len(cityCoordinates)
    initialTour = generateInitialTour(numberOfCities)
    numberOfRepetitions = input("Enter number of repetitions")
    finalTour, finalValue, repetitions = hillClimb(numberOfCities, numberOfRepetitions, distances)
    print("The best tour is: ")
    print(finalTour)

def readCoordinates(inputFile):
    cityCoordinates = []

    data = open(inputFile)

    for line in data:
        if ',' in line:
            x, y = line.strip().split(',')
            cityCoordinates.append((float(x), float(y)))

    return cityCoordinates

def calcDistances(cityCoordinates):
    distances = {}

    for i, (x1, y1) in enumerate(cityCoordinates):
        for j, (x2, y2) in enumerate(cityCoordinates):
            distances[i, j] = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distances


def evaluationFunction(distances, tour):
    tour_length = 0
    N = len(tour)
    for i in range(N - 1):
        j = (i + 1) % N
        tour_length += distances[tour[i], tour[j]]
    return tour_length


def generateSuccessors(tour):
    N = len(tour)

    randomSequence1 = [i for i in range(N)]
    shuffle(randomSequence1)
    randomSequence2 = [i for i in range(N)]
    shuffle(randomSequence2)

    for i in randomSequence1:
        for j in randomSequence2:

            if i < j:
                temp = list(tour)
                temp[i], temp[j] = tour[j], tour[i]
                yield temp


def generateInitialTour(numberOfCities):
    tour = [i for i in range(numberOfCities)]
    shuffle(tour)
    return tour


def hillClimb(numberOfCities, numberOfRepetitions, distances):
    bestTour = generateInitialTour(numberOfCities)
    bestValue = evaluationFunction(distances, bestTour)
    counter = 0

    while counter < int(numberOfRepetitions):

        moved = False

        for successor in generateSuccessors(bestTour):
            successorValue = evaluationFunction(distances, successor)

            if successorValue < bestValue:
                bestTour = successor
                bestValue = successorValue
                counter += 1
                moved = True
                break

        if moved == False:
            break
    return (bestTour, bestValue, counter)


if __name__ == "__main__":
    cityCoordinates = readCoordinates("intput2.txt")
    distances = calcDistances(cityCoordinates)
    numberOfCities = len(cityCoordinates)
    initialTour = generateInitialTour(numberOfCities)
    numberOfRepetitions = input("Enter number of repetitions")
    finalTour, finalValue, repetitions = hillClimb(numberOfCities, numberOfRepetitions, distances)
    print("The best tour is: ")
    print(finalTour)
