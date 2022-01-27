def solution(C):
    n = len(C)
    C.sort()
    for i in range(n):
        if C[i] >= n-i:
            return n-i
    return 0
print(solution([3,0,6,1,5]))