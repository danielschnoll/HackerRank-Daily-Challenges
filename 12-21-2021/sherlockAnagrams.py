#!/bin/python3

from collections import Counter

# RUNTIME:    Runs in O(n^3logn)
#             Unfortunately there's just no way around this grossly bad Big O. Finding all substrings of a
#             given string was an absolute must for this problem, and you can't escape the O(n^2) operation
#             to find them all. String slicing is an O(n) operation, which actually makes the loop O(n^3).
#             
#             We then do sorted() for each element of the substrs list, and sorted() is O(nlogn). But, the 
#             substrs list is actually of size n^2. So the second list comprehension is O(nlogn) * O(n^2)
#             resulting in an O(n^3logn) computation and an O(n^3logn) for the overall program.

#
#
# DISCUSSION: This question was pretty tough, and was really the first HR problem that really challenged me on
#             a conceptual level. The problem seems simple enough; find the pairs of anagrams that are mirrors
#             of each other. Like the problem gave the example of string MOM = [m, m] and [mo, om]. At first I
#             thought this would be like all other anagram problems I have faced before; split the string in
#             half, traverse the first half, do comparisons to the second half. That's only... half... of the
#             requirement. Or even less than half, really, since this problem is actually seeking to find the
#             anagramatic pairs of ALL possible substrings in the given string. 
#               
#             I decided to use a nested list comprehension to traverse input string s, and make a list of all
#             substrings. Two strings are anagrams of each other if, when sorted, their chars are the same.
#             And since we want to compute the number of pairs, we need to see how many substrings appear more
#             than once. They can also appear more than twice too, since you can have a string with multiple 
#             sets of repeated letters. Like in the input example 'kkkk', there are 4 substrings k, but there
#             are 6 pairs of substrings with k and k in positions (0,1), (0,2), (0,3), (1,2), (1,3), and (2,3)

#             Once again, the Counter class is our best friend. We add all sorted(substrs) to a Counter, which 
#             will give us the total number of occurrences of each anagram. We can then use the quadratic eqn
#             x*(x+1)/2 to find the total # of pairs. Going back to the 'kkkk' example, this works because str
#             k appears as a substr 4 times, but there are 6 pairs: 4*(4+1)/2 = 6. We do this for each itm in
#             the Counter of sorted substrings, returning the summation of the list of pair counts. QED.

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # find all possible sorted substrings of s
    substrs = [s[i: j] for i in range(len(s)) 
                    for j in range(i + 1, len(s) + 1)]

    # make a counter of all substr pairs (we will later evict Counter vals of 1)
    sorted_substr = Counter(["".join(sorted(s)) for s in substrs])
    
    # compute the total # of pairs of substrs, skipping items of 1 (since no pair)
    pairs = [int(itm[1]*(itm[1]-1)/2) for itm in sorted_substr.items() if itm[1]>1]
    
    return sum(pairs)

    
    
if __name__ == '__main__':
    with open('tests/input/input06.txt') as file:
        q = input()
        for i in range(q):
            s = input()
            result = sherlockAndAnagrams(s)
            print(result)
