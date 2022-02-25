#!/bin/python3

from collections import Counter

# RUNTIME:    Runs in O(n) - Counter creation is ||arr||, colloquially n. Lookup in arr
#             is a O(1) operation, and arr.index(), while O(n), is only done once.
#
# DISCUSSION: Funny enough, this problem doesn't even need a binary search despite the
#             editorial/problem statement suggesting it. This was easily solvable with
#             a greedy/two pointers approach. We make the counter for instant lookup
#             and to account for duplicates, and iterate over every i in arr checking
#             if the difference between m and arr[i] exists in the counter. This means
#             there is a locally optimal pair that exists within arr so we return i and
#             the index of that pair-value.

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    ctr = Counter(arr)
    for i in range(len(arr)):
        if ctr[m-arr[i]]:
            x = arr[i]
            if m-arr[i] == arr[i] and ctr[arr[i]] < 2:
                continue
            arr.remove(arr[i])
            return i+1, arr.index(m-x)+2

if __name__ == '__main__':
    with open('tests/input/input02.txt') as file:
       t = int(file.readline())

       for _ in range(t):
           m = int(file.readline())
           n = file.readline()
           arr = list(map(int, file.readline().rstrip().split()))

           result = icecreamParlor(m, arr)
           print(result)