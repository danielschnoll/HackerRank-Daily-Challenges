#!/bin/python3

# RUNTIME:    Runs in O(nlogn)
#
# DISCUSSION: An extremely straight forward problem. The input is a list of strings so
#             we can just sort it lexicographically with the builtin sorted() method.
#             It feels like its cheating so maybe I'll revisit this and implement some
#             kind of other sort algorithm. 

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    return sorted(unsorted, key=int)

if __name__ == '__main__':
    with open('tests/input/input08.txt') as file:
        n = int(file.readline().strip())
        unsorted = []
        for _ in range(n):
            unsorted.append(file.readline().strip())
        res = bigSorting(unsorted)
        print(res)
