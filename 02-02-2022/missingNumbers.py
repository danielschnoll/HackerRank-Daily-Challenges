#!/bin/python3

# RUNTIME:    Runs in O(nlogn) - From the sorted() call. Otherwise this would be O(n) due
#             to set operations being linear
#
# DISCUSSION: An extremely straight forward problem. Once again the Collections.Counter
#             class comes in handy! The essense of this problem is to see the total count
#             of each number in the array. We can then do a set-difference operation on
#             the two Counter objects, since set-difference creates a new set with objects
#             that are unique to set B but not set A. All that is left is to isolate the
#             .keys() and sort them so they're returned in increasing order.

from collections import Counter

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    ca = Counter(arr)
    cb = Counter(brr)
    
    return sorted((cb-ca).keys())

if __name__ == '__main__':
    with open('tests/input/input04.txt') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().split()))
        m = int(file.readline().strip())
        brr = list(map(int, file.readline().split()))
        result = missingNumbers(arr, brr)
        print(result)
   