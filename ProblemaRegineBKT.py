import time

import chess


# def read_coordinates(filename):
#     coordinates = []
#     with open(filename, "r") as file:
#         for line in file:
#             line = line.strip().split()
#             x, y = int(line[0]), int(line[1])
#             coordinates.append((x, y))
#     return coordinates

def ProblemaRegineBkt(table_sizes):
    solving_times = []
    for i in range(len(table_sizes)):
        n = table_sizes[i]
        timp = time.time()
        time.sleep(1)
        solution = solve_queens(n)
        print("Solving time for table size "+ str(n) + " :" + str(time.time() - timp - 1))

        if solution:
            print(f"Soluție pentru problema reginelor cu {n} regine:")
            # print(solution)
            matrice = [["." for _ in range(n)] for i in range(n)]
            for i in solution:
                matrice[i][solution[i]] = "Q"
            for linie in matrice:
                print(linie)

        solving_times.append(time.time() - timp - 1)
    return solving_times

def solve_queens(n):
    def is_valid(queens, col):
        for row in range(len(queens)):
            if abs(queens[row] - col) in (0, abs(row - len(queens))):
                return False
        return True

    def backtrack(queens, row):
        if row == n:
            return queens
        for col in range(n):
            if is_valid(queens, col):
                queens.append(col)
                if row == n - 1:
                    with open("output.txt", "w") as file:
                        for i in range(n):
                            file.write(f"{i} {queens[i]}\n")
                    return queens
                solution = backtrack(queens, row + 1)
                if solution:
                    return solution
                queens.pop()
        return None

    return backtrack([], 0)


if __name__ == "__main__":
    n = 8
    file = "input.txt"
    #coordinates = read_coordinates(file)
    timp = time.time()
    time.sleep(1)
    solution = solve_queens(n)
    print(time.time() - timp - 1)


    if solution:
        print(f"Soluție pentru problema reginelor cu {n} regine:")
        #print(solution)
        matrice = [["." for _ in range(n)] for i in range(n)]
        for i in solution:
            matrice[i][solution[i]] = "Q"
        for linie in matrice:
            print(linie)
    else:
        print(f"Nu există soluție pentru problema reginelor cu {n} regine.")

