def solution(S):
    if not S:
        return 1
        
    c = {
        '(' : (0, True),
        ')' : (0, False),
        '{' : (1, True),
        '}' : (1, False),
        '[' : (2, True),
        ']' : (2, False),
    }
    
    stack = list()
    for i in S:
        if c[i][1] == True:
            stack.append(c[i])
        else:
            if not stack or stack.pop()[0] != c[i][0]:
                return 0
    if stack:
        return 0
    return 1