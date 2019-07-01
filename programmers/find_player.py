def solution(p, c):
    answer = ''
    a = p.copy()
    p.sort()
    c.sort()
    n = len(c)
    
    for i in range(n):
        if p[i] != c[i]:
            answer = p[i]
            break
    if answer == '':
        answer = p[n]
    return answer