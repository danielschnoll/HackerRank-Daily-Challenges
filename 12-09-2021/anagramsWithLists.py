#!/bin/python3

from collections import Counter

# RUNTIME:    Runs in O(||lhs|| * ||rhs||) == O(||s||)
#             Iterate over each c in lhs, and "c in list()" is a linear search. Element removal is O(1)
#             
#
# DISCUSSION: This was a pretty straight forward task - We need to identify the number of chars in the LHS
#             that don't exist in the RHS. We can keep track of the total number of differing chars by
#             removing the matches from LHS, and we return the remaining length of the LHS char array
#             to get the number of chars that must change to make an anagram of the RHS

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Remove the matched char from lhs, remaining chars are ones lhs needs to change
def anagram(s):
    if len(s)%2 != 0: return -1
    lhs, rhs = list(s[:len(s)//2]), list(s[len(s)//2:])
    for char in rhs: 
        if char in lhs: lhs.remove(char)
    return len(rhs)
    
    
if __name__ == '__main__':
    with open('tests/input/input03.txt') as file:
        numInputs = int(file.readline())
        for i in range(numInputs):
            s = file.readline()
            print(anagram(s))