QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem?isFullScreen=true

# This problem is a programming version of Problem 11 from projecteuler.net

SOLUTION:-

import sys
def max_grid_product(grid):
    max_product = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols - 3):
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            max_product = max(max_product, product)
    for i in range(rows - 3):
        for j in range(cols):
            product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            max_product = max(max_product, product)
    for i in range(rows - 3):
        for j in range(cols - 3):
            product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            max_product = max(max_product, product)
    for i in range(3, rows):
        for j in range(cols - 3):
            product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            max_product = max(max_product, product)
    return max_product
def main():
    grid = []
    for _ in range(20):
        row = list(map(int, input().strip().split()))
        grid.append(row)
    result = max_grid_product(grid)
    print(result)
if __name__ == "__main__":
    main()
