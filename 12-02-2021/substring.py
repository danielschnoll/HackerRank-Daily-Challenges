#!/bin/python3
import os

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(st):
    substring = "hackerrank"
    index = 0
    # Worst case scenario function runs in O(n)
    for c in st:
        # Increment index to check for first occurrence of the next char
        if c == substring[index]: index += 1
        # Full substring is found before end of checkstring
        if index == len(substring): return "YES"
    # Substring not found
    return "NO"
    

if __name__ == '__main__':
    with open('tests/input/input03.txt') as file:
        numInputs = int(file.readline())
        for i in range(numInputs):
            s = file.readline()
            print(hackerrankInString(s))