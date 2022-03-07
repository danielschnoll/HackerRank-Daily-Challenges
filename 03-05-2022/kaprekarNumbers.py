#!/bin/python3

# RUNTIME:    Runs in O(p-q) ~= O(n)
#
# DISCUSSION: Iterate over each element in the range, convert it to a string and split
#             it in half. If the current x = lhs + rhs of the squared results, print.

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    output = False
    for x in range(p, q+1):
        square, lsq = str(x**2), len(str(x**2))
        rhs = 0 if square[:lsq//2] == '' else int(square[:lsq//2])
        lhs = int(square[lsq//2:])
        if x == lhs + rhs:
            output = True
            print(x, "", end="")
    if not output:
        print("INVALID RANGE")

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:

        p = int(file.readline())
        q = int(file.readline())

        kaprekarNumbers(p, q)