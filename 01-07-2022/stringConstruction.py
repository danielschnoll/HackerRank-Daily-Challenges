#!/bin/python3

# RUNTIME:    Runs in O(||s||) - visit each char in s once to add to the set()
#
#
# DISCUSSION: This problem seems harder than it truly is... its actually fairly trivial.
#             The whole idea of "copying" as noted in the problem description is really
#             just adding items to a set. The "cost" of 0 refers to the addition of a
#             duplicate item, which in a python hashset, isn't allowed. So just add all
#             elements from string s to a set to get the "min cost" of "copying".

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    with open('tests/input/input12.txt') as file:
        n = int(file.readline().strip())
        for _ in range(n):
            s = file.readline().strip()
            print(stringConstruction(s))