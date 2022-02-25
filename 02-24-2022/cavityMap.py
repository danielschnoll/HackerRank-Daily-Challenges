#!/bin/python3

# RUNTIME:    Runs in O((n-2)^2) - Must loop over every char but boundary boxed by the
#             perimeter, so we're -2 from both the L and W... ex. a 3x3 grid turns into
#             a 1x1, a 7x7 turns into a 5x5, etc.
#
# DISCUSSION: Pretty straight forward problem. There is no better way to do this other
#             than looping through all elements of the grid, since we need to compare
#             each element to its neighbors. Some simple string-list manipulation and
#             we have our answer.

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and\
                grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                x = list(grid[i])
                x[j] = 'X'
                grid[i] = ''.join(x)
    return grid

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:
        n = int(file.readline())
        g = []
        for _ in range(n):
            g.append(file.readline().rstrip())
        result = cavityMap(g)
        print(*result, sep='\n')
