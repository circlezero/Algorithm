def solution(P, C):
    ans = P // 2
    if ans > C:
        ans = C
    return ans