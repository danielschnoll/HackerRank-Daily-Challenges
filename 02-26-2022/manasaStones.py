#!/bin/python3

# RUNTIME:    Runs in O(nlogn) - Applies the formula to each element, O(n)
#                              - Converts list to a set, sorts the set O(nlogn)
#
# DISCUSSION: Pretty straight forward problem. There is no better way to do this other
#             than looping through all elements of the grid, since we need to apply the
#             summation formula to each. The answer has us return it in increasing order
#             so we need to apply sorted(), which is O(nlogn)

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Formula a*i+b*(n-1-i) will get us all possible sums
    # Add this to a set, and sort the set
    return sorted(set([a*i+b*(n-1-i) for i in range(n)]))

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:
        t = int(file.readline())
        for _ in range(t):
            n = int(file.readline())
            a = int(file.readline())
            b = int(file.readline())
            res = stones(n, a, b)
            print(res)