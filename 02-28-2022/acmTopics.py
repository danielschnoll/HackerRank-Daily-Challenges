#!/bin/python3

from itertools import combinations

# RUNTIME:    Runs in O(n^3) - We iterate over the list in two for loops to find the
#             total # of pairs in the topics arr
#
# DISCUSSION: For this problem I initially tried to use the combinations function, but
#             this was failing test cases due to timeout issues. Clearly this was too
#             memory intensive, so I opted for a traditional loop-twice-to-find-all-pairs
#             approach. For the inner loop, we are effectively doing the summation of n 
#             since each iteration decreases the looping range by 1... (n + n-1 + n-2...)
#             This is encased in an outer for loop, n, so we get n * (n(n-1)/2) ~= n^3.
#             Gross...

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # A very pythonic way that keeps timing out
    # teamKnowledge = [sum([int(i[0]) or int(i[1])
    #                     for i in zip(*pair)])
    #                         for pair in combinations(topic, 2)] 
    # return [max(teamKnowledge), teamKnowledge.count(max(teamKnowledge))]
    
    maxTopic=0
    maxTeam=0
    for first in range(len(topic)):
        for second in range(first+1,len(topic)):
            # convert each pair to a binary int, and take their xor
            maxMatch = bin(int(topic[first],2) | int(topic[second],2)).count('1')
            # see which maxMatch is bigger - our memoized one or the current maxMatch
            if maxMatch > maxTopic:
                maxTopic = maxMatch
                maxTeam = 1 # reset the counter
            elif maxMatch == maxTopic:
                maxTeam += 1
    return [maxTopic, maxTeam]

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:
        t = file.readline().split()
        n = int(t[0])
        topics = []
        for _ in range(n):
            topic = file.readline()
            topics.append(topic)
            arr = list(map(int, file.readline().rstrip().split()))

        result = acmTeam(topics)
        print(result)