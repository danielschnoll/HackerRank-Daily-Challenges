#!/bin/python3

# RUNTIME:    Runs in O(n) - Set intersection operation is linear
#
# DISCUSSION: This problem was facilitated greatly by the fact that there is one
#             small constraint that is easily glossed over: All arr_i in arr are
#             *unique integers*. What this means is we can create two sets, one
#             that is unmodified and one that is incremented by k for each int.
#             Taking the intersection of these two sets will yield all overlapping
#             ints, which are simply the ones who have a difference of k.

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    s_arr = set(arr)
    s_k_arr = set([v + k for v in arr])
    return len(s_arr & s_k_arr)

if __name__ == '__main__':
    with open('tests/input/input04.txt') as file:
        inp = file.readline().rstrip().split()

        k = int(inp[1])
        arr = list(map(int, file.readline().rstrip().split()))

        result = pairs(k, arr)
        print(result)