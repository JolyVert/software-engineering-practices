import random
import time

N = 10


def create_grid():
    return [[random.randint(0, 1) for _ in range(N)] for _ in range(N)]


def print_grid(grid):
    for row in grid:
        for cell in row:
            print("O" if cell == 1 else ".", end="" )
        print()
    print("\n" * 2)


def count_neighbors(grid, i, j):
    neighbors = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            if 0 <= x < N and 0 <= y < N:
                neighbors += grid[x][y]
    return neighbors


def next_generation(grid):
    new_grid = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid


grid = create_grid()

while True:
    print_grid(grid)
    grid = next_generation(grid)
    time.sleep(1)