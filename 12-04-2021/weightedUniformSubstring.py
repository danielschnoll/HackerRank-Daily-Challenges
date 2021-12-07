#!/bin/python3

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # variables
    substr_totals = set() # use a set instead of dict to save memory space
    ret_arr = [] 
    last_char = s[0]
    current_uniform_substr = ''
    
    # Function runs in O(n), only visit each c once; build substr and dynamically save for each pass
    for c in s:
        # dynamically build the current uniform substr based on prev char
        if c == last_char: 
            current_uniform_substr += c
        else: 
            current_uniform_substr = c
        # ord() returns ASCII value for the given char, -96 to get alphanumeric position
        val = (ord(c)-96) * len(current_uniform_substr)
        substr_totals.add(val)
        last_char = c
    
    # build the return arr
    for query in queries:
        if query in substr_totals:
            ret_arr.append("Yes")
        else:
            ret_arr.append("No")
    
    return ret_arr
    
if __name__ == '__main__':
    with open('tests/input/input5.txt') as file:
        st = file.readline()
        numInput = int(file.readline().strip())
        queries = []
        for i in range(numInput):
            queries.append(int(file.readline().strip()))
    print(weightedUniformStrings(st, queries))