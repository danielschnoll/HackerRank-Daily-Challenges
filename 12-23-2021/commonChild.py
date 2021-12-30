#!/bin/python3

# RUNTIME:    Runs in O(n*m)
#             Enumerating over the two strings, and takes up polynomial ~n^2 memory. I will
#             likely try to optimize this with a caching implementation that only preserves
#             the two actively-compared rows in the DP memoization table
#             
#             Complexity and optimization details can be found on the LCS wiki page
#             https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Complexity
#
#
# DISCUSSION: This is a straight forward implementation of the Longest Common Substring problem.
#             It utilizes a concept called memoization, or when the solutions of subproblems are 
#             saved for future use. The 2D table is what we use to store the subproblems, and the
#             algorithm works by maintaining knowledge of the current count of matching chars.
#             Each char that matches in the string increases the subtotal, and by the end of the
#             table traversal, we can obtain the length of the longest subsequence by simply 
#             returning the value at the final [row][col] index.
#             
#             More info on LCS: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
#             HackerRank intro to DP: https://www.hackerrank.com/challenges/common-child/topics

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Declare the memoization table for use in dynamic programming
    tbl = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

    # iterate the two strings and update the [i][j] location accordingly
    for i, c1 in enumerate(s1, 1):
        for j, c2 in enumerate(s2, 1):
            if c1 == c2: tbl[i][j] = tbl[i-1][j-1] + 1
            else: tbl[i][j] = max(tbl[i-1][j], tbl[i][j-1])
                
    return tbl[len(s1)][len(s2)]

if __name__ == '__main__':
    with open('tests/input/input14.txt') as file:
        i1 = input()
        i2 = input()
        res = commonChild(i1,i2)
        print(res)
