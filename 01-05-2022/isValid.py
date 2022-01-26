#!/bin/python3

from collections import Counter

# RUNTIME:    Runs in O(||s||) or O(n) due to the creation of the Counter object
#
#
# DISCUSSION: This was a fairly straight forward problem. It really came down to some tricks
#             in set manipulation. We create the Counter for the initial frequencies, then 
#             see how frequent each frequency is. Then we run through the following checks:
#             - The valFrequency Counter must be exactly 2, or 1, values long.
#             - If 1, all chars are the same and the string is valid 
#             - If 2, one of the values must be 1 (ie only 1 char is the odd-one out) AND
#               the odd-one out is either a value of 1 OR the difference between the two is 1
#               - the former suggests only 1 of that char exists, a simple removal
#               - the latter suggests the minimal string occurs only once more than the max
#                 and a single removal would make them have the same frequencies


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    charFrequency = Counter(s)
    valFrequency = Counter(charFrequency.values())
    
    if len(valFrequency.values()) == 1:
        return "YES"

    if len(valFrequency.values()) > 2:
        return "NO"

    keys = valFrequency.keys()
    if 1 in valFrequency.values() and \
        (valFrequency[min(keys)]== 1 or max(keys)-min(keys)==1):
        return "YES"
    else:
        return "NO"

    
if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:
        s = file.readline()
        res = isValid(s)
        print(res)