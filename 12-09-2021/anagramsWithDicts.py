#!/bin/python3

from collections import Counter

# RUNTIME:    Runs in O(||s||)
#             The collections.Counter class is a wrapper around the dictionary data structure. When called it 
#             instantiates a dictionary of size s, and initializes each value to the number of occurrences of 
#             each key. Dict instantiation depends on ||s||. 
#             Set operations work on dictionaries, so set difference operation is O(||lhs||+||rhs||). We then
#             sum the diff.values(), an O(n) operation that will be at most equal in size to ||s||//2 assuming
#             worst case where every element in LHS needs to be replaced to match RHS
#
#
# DISCUSSION: My initial design choice was to do set operations, get the difference between the two anagram halves
#             and return the size of the difference. Which is what I ended up doing in this solution anyway, but I
#             ran into a conceptual issue when I realized using a set() would exclude duplicate chars, so I needed 
#             a multiset. Not wanting to build my own data structure, I opted to scrap my initial idea and go with 
#             the implementation in anagramsWithLists, which is probably a more traditional linear approach to the
#             problem anyway. However, after some brief research I discovered Python has a multiset implementation 
#             in the collections library in the form of Counter. So, wanting to make a fancier "Pythonic" version 
#             of my solution, I opted for this simple 3 line program. It instantiates the diff dict immediately by 
#             foregoing the intermediate LHS and RHS variables, and then returns the return value from sum().
#             Very elegant if I had to say so myself!

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s)%2 != 0: return -1
    diff = Counter(s[:len(s)//2]) - Counter(s[len(s)//2:])
    return sum(diff.values())
    
    
if __name__ == '__main__':
    with open('tests/input/input03.txt') as file:
        numInputs = int(file.readline())
        for i in range(numInputs):
            s = file.readline()
            print(anagram(s))
