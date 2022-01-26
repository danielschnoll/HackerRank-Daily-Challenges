#!/bin/python3

from collections import Counter

# RUNTIME:    Runs in O(4*||gene||), or approx. O(n) where n is ||gene||
#             While loop is for the length of gene, and each call to balanced is a
#             for-loop of length 4
#
#
# DISCUSSION: The problem is an implementation of the Two Pointers/Sliding window algorithm. 
#             The idea is to map the frequency of each char in the string and keep track in 
#             real time as you add and remove chars in the string. As we slide across the 
#             string we increase the window size to the right by increasing 'end' until the 
#             frequency of each remaining char is less than or equal to n/4. We then store 
#             that window size. After that we reduce the window size from the left by 
#             increasing i, again until the frequency of each char is less than or equal to 
#             n/4. The lesser of the two window sizes is what gets printed
#             https://www.geeksforgeeks.org/two-pointers-technique/ 
#               

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def balanced(ln, ctr):
    for k, v in ctr.items():
        if v > ln:
            return False
    return True

def steadyGene(gene):
    l = len(gene) // 4
    alleles = Counter(gene)
    start=0
    end=0
    count=999999
    while(start<len(gene) and end<len(gene)):
        if not balanced(l,alleles):
            alleles[gene[end]]-=1
            end+=1
        else:
            count=min(count,end-start)
            alleles[gene[start]]+=1
            start+=1    
    return count

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:
        n = file.readline()
        gene = file.readline()
        res = steadyGene(gene)
        print(res)
