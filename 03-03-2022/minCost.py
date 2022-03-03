#!/bin/python3

# RUNTIME:    Runs in O(n) - Well, n is really 4 total elements so its as close to const
#             time as possible, but we still have to check all elements in the min. Let's
#             just call it O(1) and shake on it...
#
# DISCUSSION: Problem statement made this way more confusing than it needed to be. Basically
#             z is a constant that can increase the "cost" of the gifts. So for example, if
#             z = 3, and bc = 5 and wc = 10, we will buy b gifts at min cost 5, and w gifts
#             at min cost 8. The z allows us to substitute a higher cost, ex. wc, for the
#             lower cost, ex. bc, at the cost of z. So we just need to take the min of bc,
#             wc, bc+z, and wc+z to get how many substituions we can make.

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    return b*min(bc, wc+z) + w*min(wc,bc+z)

if __name__ == '__main__':
    with open('tests/input/input00.txt') as file:

        t = int(file.readline())

        for _ in range(t):
            fl = file.readline().rstrip().split()
            b, w = int(fl[0]), int(fl[1])

            sl = file.readline().rstrip().split()
            bc, wc, z = int(sl[0]), int(sl[1]), int(sl[2])

            result = taumBday(b, w, bc, wc, z)

            print(result)