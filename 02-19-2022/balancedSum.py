#!/bin/python3

# RUNTIME:    Runs in O(n) - Largest operation is the sum of the array
#
# DISCUSSION: This problem uses the two-pointers method. We sum the input array
#             and then subtract the ith value from the sum. This way we are
#             "looking" at the sum to the right of the ith value without ever
#             recomputing the sum. We can then add on the ith value to the left
#             pointer and proceed the loop. We add the value AFTER comparison
#             because the present ith value is not included in the running sum

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    left = 0
    right = sum(arr)
    for i in range(len(arr)):
        right -= arr[i]
        if left == right:
            return "YES"
        left += arr[i]
    return "NO"

if __name__ == '__main__':
    with open('tests/input/input07.txt') as file:
        inp = int(file.readline())

        for _ in range(inp):
            k = int(file.readline())
            arr = list(map(int, file.readline().rstrip().split()))

            result = balancedSums(arr)
            print(result)