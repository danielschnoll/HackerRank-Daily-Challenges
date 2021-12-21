#!/bin/python3

from collections import Counter

# RUNTIME:    Runs in O(||s1|| + ||s2||)
#             The collections.Counter class is a wrapper around the dictionary data structure. Instantiation depends
#             on ||s||. Set operations work on dictionaries, and set difference operation is O(||s1||+||s2||). We do
#             this twice. Then, sum the dict.values(), an O(n) operation that will at worst each be equal in size to
#             s1 and s2 respectively
#
#
# DISCUSSION: This problem is very similar to the anagrams problem from 12/09/2021. The main idea is to take the diff
#             between the strings and see which chars they have in common. We need a multiset for this so we can do
#             set operations with duplicates. We take the difference of s1 - s2 and s2 - s1, and the end result is the
#             total # of chars that are unique to both s1 and s2. This is effectively the symmetric difference ( ^ )
#             but the multiset class doesn't have a functional ^ operator at the moment.

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    diffS1_S2 = Counter(s1) - Counter(s2)
    diffS2_S1 = Counter(s2) - Counter(s1)
    return sum(diffS1_S2.values()) + sum(diffS2_S1.values())

if __name__ == '__main__':
    with open('tests/input/input15.txt') as file:
        s1 = input()
        s2 = input()
        print(makingAnagrams(s1, s2))