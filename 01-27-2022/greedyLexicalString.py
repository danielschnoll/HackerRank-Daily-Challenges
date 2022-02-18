#!/bin/python3

# RUNTIME:    Runs in O(max(a, b))
#
# DISCUSSION: I had two solutions to this. The first approach was to take a greedy recusive
#             approach where so long as the strings weren't empty, we grab the 0 index char
#             & compare their lexical value. If they are equal, advance the string "stack"
#             by passing the sliced string back into the function. But this proved to be 
#             memory intensive, and there's a significantly easier approach - simply check 
#             to see that the strings are not at their ends and use string slicing to check
#             remainder(a) < remainder(b). The equality operators operate on lexicograpical
#             ordering already, so we don't need to copy the string slice to a new variable
#             like I was in my recursive solution. This version cuts back on the memory usage
#             substantially, and passes all test cases!      

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    answer = ''
    
    # Add the ~ as a terminal case
    a += '~'
    b += '~'
    i = j = 0
    while a[i] != '~' or b[j] != '~':
        # if a is not terminal and remainder(a) < remainder(b)
        if a[i] != '~' and a[i:] < b[j:]:
            answer += a[i]
            i += 1
        # b is less, append b
        else:
            answer += b[j]
            j += 1
    return answer

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:
        t = int(file.readline().strip())

        for _ in range(t):
            str_a = file.readline().strip()
            str_b = file.readline().strip()
            res = morganAndString(str_a, str_b)

            print(res)