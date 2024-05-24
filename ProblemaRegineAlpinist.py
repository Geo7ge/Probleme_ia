import time
from random import randint

# N = 8

def ProblemaRegineAlp(table_sizes):
    solving_times = []
    for i in range(len(table_sizes)):
        n = table_sizes[i]
        state = [0] * n
        board = [[0 for i in range(n)] for j in range(n)]
        configureRandomly(board, state, n)
        timp = time.time()
        time.sleep(1)
        hillClimbing(board, state, n)
        print("Solving time for table size "+ str(n) + " :" + str(time.time() - timp - 1))
        solving_times.append(time.time() - timp - 1)
        matrice = [["." for _ in range(n)] for i in range(n)]
    return solving_times

def configureRandomly(board, state, N):
    for i in range(N):

        state[i] = randint(0, 100000) % N
        board[state[i]][i] = 1


def printBoard(board, N):
    for i in range(N):
        print(*board[i])


def printState(state):
    print(*state)


def compareStates(state1, state2, N):
    for i in range(N):
        if (state1[i] != state2[i]):
            return False

    return True


def fill(board, value, N):
    for i in range(N):
        for j in range(N):
            board[i][j] = value


def calculateObjective(board, state, N):
    attacking = 0
    for i in range(N):
        row = state[i]
        col = i - 1
        while (col >= 0 and board[row][col] != 1):
            col -= 1

        if (col >= 0 and board[row][col] == 1):
            attacking += 1

        row = state[i]
        col = i + 1
        while (col < N and board[row][col] != 1):
            col += 1

        if (col < N and board[row][col] == 1):
            attacking += 1

        row = state[i] - 1
        col = i - 1
        while (col >= 0 and row >= 0 and board[row][col] != 1):
            col -= 1
            row -= 1

        if (col >= 0 and row >= 0 and board[row][col] == 1):
            attacking += 1

        row = state[i] + 1
        col = i + 1
        while (col < N and row < N and board[row][col] != 1):
            col += 1
            row += 1

        if (col < N and row < N and board[row][col] == 1):
            attacking += 1

        row = state[i] + 1
        col = i - 1
        while (col >= 0 and row < N and board[row][col] != 1):
            col -= 1
            row += 1

        if (col >= 0 and row < N and board[row][col] == 1):
            attacking += 1

        row = state[i] - 1
        col = i + 1
        while (col < N and row >= 0 and board[row][col] != 1):
            col += 1
            row -= 1

        if (col < N and row >= 0 and board[row][col] == 1):
            attacking += 1

    return int(attacking / 2)


def generateBoard(board, state, N):
    fill(board, 0, N)
    for i in range(N):
        board[state[i]][i] = 1


def copyState(state1, state2, N):
    for i in range(N):
        state1[i] = state2[i]


def getNeighbour(board, state, N):
    opBoard = [[0 for _ in range(N)] for _ in range(N)]
    opState = [0 for _ in range(N)]

    copyState(opState, state, N)
    generateBoard(opBoard, opState, N)

    opObjective = calculateObjective(opBoard, opState, N)
    NeighbourBoard = [[0 for _ in range(N)] for _ in range(N)]

    NeighbourState = [0 for _ in range(N)]
    copyState(NeighbourState, state, N)
    generateBoard(NeighbourBoard, NeighbourState, N)
    for i in range(N):
        for j in range(N):

            if (j != state[i]):

                NeighbourState[i] = j
                NeighbourBoard[NeighbourState[i]][i] = 1
                NeighbourBoard[state[i]][i] = 0
                temp = calculateObjective(NeighbourBoard, NeighbourState, N)
                if (temp <= opObjective):
                    opObjective = temp
                    copyState(opState, NeighbourState, N)
                    generateBoard(opBoard, opState, N)

                NeighbourBoard[NeighbourState[i]][i] = 0
                NeighbourState[i] = state[i]
                NeighbourBoard[state[i]][i] = 1
    copyState(state, opState, N)
    fill(board, 0, N)
    generateBoard(board, state, N)


def hillClimbing(board, state, N):
    neighbourBoard = [[0 for _ in range(N)] for _ in range(N)]
    neighbourState = [0 for _ in range(N)]

    copyState(neighbourState, state, N)
    generateBoard(neighbourBoard, neighbourState, N)

    while True:

        copyState(state, neighbourState, N)
        generateBoard(board, state, N)

        getNeighbour(neighbourBoard, neighbourState, N)

        if (compareStates(state, neighbourState, N)):

            printBoard(board, N)
            break

        elif (calculateObjective(board, state, N) == calculateObjective(neighbourBoard, neighbourState, N)):

            neighbourState[randint(0, 100000) % N] = randint(0, 100000) % N
            generateBoard(neighbourBoard, neighbourState, N)


if __name__ == "__main__":
    state = [0] * N
    board = [[0 for _ in range(N)] for _ in range(N)]

    configureRandomly(board, state)

    hillClimbing(board, state)
