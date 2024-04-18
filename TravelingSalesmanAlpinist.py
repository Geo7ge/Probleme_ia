# the following piece of code finds a solution to the traveling salesman problem using the Hill Climbing Algorithm
# for this it reads the coordinates of cities from a user generated input file and prints the best tour for the salesman
# as per other conditions of the iteration. The output is something like 2-4-3-1-0-2 which represent the tour starting from
# city 2 and visiting cities 4,3,1,0 in that order and returning to 2. Here the cities as numbered in the order in which they
# appear in the input file

import sys
from random import shuffle
from math import *


# this function reads the co-ordinates of the various cities in the Travelling Salesman Problem
# and saves them in a 2D list cityCoordinates
def readCoordinates(inputFile):
    cityCoordinates = []

    # creating file object 'data' to read the coordinates
    data = open(inputFile)

    # looping through the file and avoiding empty last lines if any. Returing the 2D list containing city coordinates
    for line in data:
        if ',' in line:
            x, y = line.strip().split(',')
            cityCoordinates.append((float(x), float(y)))

    return cityCoordinates


# the following function takes in the all city coordinates and generates a 'distances' dictionary which contains the
# Eucleidian (Straight line distance/ Cartesian distance) distances between each pair of city present in the problem.
# In our case, distances for (i,j) will be same as (j,i)
def calcDistances(cityCoordinates):
    distances = {}

    for i, (x1, y1) in enumerate(cityCoordinates):
        for j, (x2, y2) in enumerate(cityCoordinates):
            # calculate straight line distance
            distances[i, j] = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distances


# the following function takes in a given tour of cities and returns the tour length as the value of evaluation function
# of that particular tour. It does so by calculating the total tour length. the tour length takes into account that
# the salesman returns to the city he started from
def evaluationFunction(distances, tour):
    tour_length = 0
    N = len(tour)
    for i in range(N - 1):
        j = (i + 1) % N
        tour_length += distances[tour[i], tour[j]]
    return tour_length


# the following function is a generator function which generates all pairs of successors of the initial tour
# 'yield' is used to avoid saving all successors in the memory instead yielding them as and when required
def generateSuccessors(tour):
    N = len(tour)

    # generate 2 random sequences
    randomSequence1 = [i for i in range(N)]
    shuffle(randomSequence1)
    randomSequence2 = [i for i in range(N)]
    shuffle(randomSequence2)

    # this generates all successors of the initial tour and yields them
    for i in randomSequence1:
        for j in randomSequence2:

            # to avoid swapping same pair twice
            if i < j:
                temp = list(tour)
                temp[i], temp[j] = tour[j], tour[i]
                yield temp


# the following function generates a random initial tour to begin the hill climbing with
def generateInitialTour(numberOfCities):
    tour = [i for i in range(numberOfCities)]
    shuffle(tour)
    return tour


# the following is the hill climbing function which compares all the possible successors of a position on the hill and chooses
# the best among them. It then compares the current value with the best neighbor. If the neoghbor is better, it becomes the
# current value, if not the ascent is stopped and the current value is returned as the ideal value
def hillClimb(numberOfCities, numberOfRepetitions, distances):
    # assign initial tour as the best
    bestTour = generateInitialTour(numberOfCities)
    bestValue = evaluationFunction(distances, bestTour)
    counter = 0

    # repeating the hill climbing algorithm for the required number of repetitions
    while counter < int(numberOfRepetitions):

        # flag bit indicating if the value has moved uphill
        moved = False

        # checking for all successors of the current value by iterating through the generator
        for successor in generateSuccessors(bestTour):
            successorValue = evaluationFunction(distances, successor)

            # moving uphill if successir is better than current value
            if successorValue < bestValue:
                bestTour = successor
                bestValue = successorValue
                counter += 1
                moved = True
                break
        # none of the successor has a better value. Algorithm is stopped than
        if moved == False:
            break

    # returning the best tour and the value
    return (bestTour, bestValue, counter)


# reading the user inpit for city coordinates
if __name__ == "__main__":
    cityCoordinates = readCoordinates("intput2.txt")
    distances = calcDistances(cityCoordinates)
    numberOfCities = len(cityCoordinates)
    initialTour = generateInitialTour(numberOfCities)
    numberOfRepetitions = input("Enter number of repetitions")
    finalTour, finalValue, repetitions = hillClimb(numberOfCities, numberOfRepetitions, distances)
    print("The best tour is: ")
    print(finalTour)
