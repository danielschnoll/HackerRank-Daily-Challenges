#!/bin/python3

# RUNTIME:    Runs in O(||s||//2)
#
#
# DISCUSSION: This was a fairly straight forward problem. There are a few rules to adhere 
#             by for the value pair changes: When the pairs are mismatched, either set 
#             them both to 9 if >1 changes are left, or choose the max. When the pairs are 
#             matching, if neither are 9 and we have >1 changes, set both to 9. Otherwise, 
#             both are already 9. I had another version of this solution but it kept 
#             missing 4 test cases. After looking at the discussion I realized it was 
#             because I was overcounting the remaining swaps. This logic flow was suggested 
#             in the comments and upon trying it I managed to pass all tests. My old sol'n
#             has been added to the repo to for documentation purposes

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    lhs = list(s[:n//2])
    rhs = list(s[n//2+1:][::-1]) if n % 2 == 1 else list(s[n//2:][::-1])
    totalDiff = 0
    for i in range(len(lhs)):
        if(lhs[i] != rhs[i]):
            totalDiff += 1
    # base case: more changes possible than k allowed changes
    if totalDiff > k:
        return '-1'
    remaining = k - totalDiff
 
    # base case: only one int
    if n == 1 and k > 0:
        return '9'
    # base case: num allowed changes is larger than the string itself
    if k >= n:
        return '9'*n

    for i in range(len(lhs)):
        # Mismatched pair and neither are 9
        if lhs[i] != rhs[i] and remaining != 0:
            if s[i] != '9' and rhs[i] != '9':
                remaining -= 1
            lhs[i] = rhs[i] = '9'
        # Mismatched pair and no remaining pair changes
        elif lhs[i] != rhs[i] and remaining == 0:
            lhs[i] = rhs[i] = max(lhs[i],rhs[i])
        # Matching pair and neither are 9
        elif lhs[i] == rhs[i] and remaining > 1 and lhs[i] != '9':
            remaining -= 2
            lhs[i] = rhs[i] = '9'
        # Both are 9
        else:
            continue
    if n % 2 == 0:
        ans = "".join(lhs + (rhs[::-1]))
    if n % 2 == 1:
        mid = ['9'] if remaining > 0 else [s[n//2]]
        ans = "".join(lhs + mid + (rhs[::-1]))
    return ans

if __name__ == '__main__':
    with open('tests/input/input10.txt') as file:
        l = file.readline().strip().split()
        n = int(l[0])
        k = int(l[1])
        s = file.readline().strip()
        res = highestValuePalindrome(s, n, k)

        print(res)