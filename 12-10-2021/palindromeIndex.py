#!/bin/python3

# RUNTIME:    Runs in O(||s||)
#             s[:i] + s[i+1:] is string concatenation, an O(s1 +s1) ~= O(||s||) operation
#             
#
# DISCUSSION: Remove the char that we identify is not identical on the string's mirrored half. If
#             the concatenated string is a palindrome, return i; otherwise, return the index of the
#             mirrored half (because removing the char at the mirrored index will be a palindrome)

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    if s == s[::-1]: return -1
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            tmp = s[:i] + s[i+1:] 
            if tmp[:] == tmp[::-1]: return i
            return len(s)-1-i
    return -1

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:
        numInputs = int(file.readline())
        for i in range(numInputs):
            s = file.readline()
            print(palindromeIndex(s))
