#!/bin/python3

# RUNTIME:    Runs in ~O(||s||//2 * ||s||) ~= O(||s||^2)
#             Use floor div because we never need to see second half of string,
#             Inner while-loop does ~||s|| iterations per outer loop iteration,
#             (Technically less because its adding 1 part, then 2 parts, 3 parts until ||s||//2)
#
#
# DISCUSSION: This was actually a pretty hard problem. Initially I thought of doing something where I recursively pop off
#             the first element and try building sequences based on the next elem in the array, doing equality comparisons
#             along the way, but I quickly realized that isn't manageable. I turned to the discussion forum and people 
#             mentioned searching only half of the given string, and iterating over slices of the half in 
#             increasing size, which led me to the solution I have below

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s): 
    # Base case, 1 is not beautiful
    if len(s)==1:
        return 'NO'
    
    # Ex: 900901, when we split in half we add '901' to the base substr to get back 900901
    for i in range(1,len(s)//2+1):
        
        # Build the string slices
        firstInSequence, nextInSequence = int(s[0:i]), int(s[0:i])
        substr=s[0:i]
        
        # Compound substr with nextInSequence until initial string length
        # is rebuilt with the sequencing, then check if the rebuilt substr == s
        # (loop will do approximately ||s|| iterations)
        while len(substr)+len(str(int(nextInSequence)+1)) <= len(s):
            nextInSequence +=1
            substr += str(nextInSequence)
        if substr == s:
            return 'YES '+str(firstInSequence)
    return 'NO'    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))
