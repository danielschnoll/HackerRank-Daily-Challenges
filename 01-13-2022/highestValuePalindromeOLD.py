def highestValuePalindrome(s, n, k):
    # base case: only one int
    if n == 1 and k > 0:
        return '9'
    # base case: num allowed changes is larger than the string itself
    if k >= n:
        return '9'*n

    lhs = list(s[:n//2])
    rhs = list(s[n//2+1:][::-1]) if n % 2 == 1 else list(s[n//2:][::-1])
    remaining = k

    for i in range(len(lhs)):
        left = lhs[i]
        right = rhs[i]
        # Matching pair but not maximal
        if left == right:
            # They are both 9
            if left == '9':
                continue
            # Neither are 9, both need to be replaced (ex. 3 and 3)
            elif remaining >= 2:
                lhs[i] = rhs[i] = '9'
                remaining -= 2
        # Mismatched pair
        elif left != right:
            # Change only rhs
            if left == '9' and remaining >= 1:
                rhs[i] = '9'
                remaining -= 1
            # Change only lhs
            elif right == '9' and remaining >= 1:
                lhs[i] = '9'
                remaining -= 1
            # Change both (ex. 3 and 6)
            else:
                if remaining >= 2:
                    lhs[i] = rhs[i] = '9'
                    remaining -= 2
                # Only one last change is possible, choose the max
                elif remaining == 1:
                    maxVal = max(int(lhs[i]), int(rhs[i]))
                    lhs[i] = rhs[i] = str(maxVal)
                    remaining -= 1
                # No changes left, fail the string
                elif remaining == 0:
                    return '-1'
                
    if n % 2 == 0:
        ans = "".join(lhs + (rhs[::-1]))
    if n % 2 == 1:
        mid = ['9'] if remaining > 0 else [s[n//2]]
        ans = "".join(lhs + mid + (rhs[::-1]))
    return ans