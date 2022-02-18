def helpPop(s_a, s_b):
    if len(s_a) > 0 and len(s_b) > 0:
        currA = s_a[0]
        currB = s_b[0]
        
        if currA < currB:
            return "A"
        elif currB < currA:
            return "B"
    
        # Letters are equal, so we'll advance the stack so we peak at the next letter.
        # The idea is to return the stack that eventually offers the min letter
        else:
            return helpPop(s_a[1:], s_b[1:])
        
    elif len(s_a) > 0 and len(s_b) == 0:
        return "A"
    elif len(s_b) > 0 and len (s_a) == 0:
        return "B"
    # strings are equal all the way to the end, choice doesn't matter
    else:
        return "A"


def morganAndString(a, b):
    
    l = len(a) + len(b)
    minString = ""
    a += "z"
    b += "z"
    
    for _ in range(l+2):
        
        ret = helpPop(a, b)

        if ret == "A":
            minString += a[0]
            a = a[1:]
        elif ret == "B":
            minString += b[0]
            b = b[1:]
        
    return minString