#!/bin/python3

# RUNTIME:    Runs in ~O(1) - Dict lookup is O(1) and str concatenation is O(||s1|| + ||s2||)
#             We're talking nominal input sizes here, so for simplicity its O(1)
#
# DISCUSSION: Why is this even a question? It was just annoying.

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    d = {
        00: 'o\' clock',
        15: 'quarter past',
        30: 'half past',
        45: 'quarter to',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty'
    }
    
    wordH = d[h]
    wordM = d.get(m)
    
    if m == 00:
        return wordH + ' ' + wordM
    if m == 1:
        wordM = 'one minute past '
    if m == 15 or m == 30:
        return wordM + ' ' + wordH
    if m == 45:
        return wordM + ' ' + d[h+1]
    elif not wordM:
        if m < 30:
            wordM = d[20] + ' ' + d[m-20] + ' minutes past '
        if m > 30 and m != 45:
            if 60-m > 20:
                wordM = d[20] + ' ' + d[m-30] + ' minutes to '
            else:
                wordM = d[60-m] + ' minutes to '
    
    wordH = d[h+1] if m>30 else d[h]
    return wordM + wordH

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:

        h = int(file.readline())
        m = int(file.readline())

        print(timeInWords(h,m))