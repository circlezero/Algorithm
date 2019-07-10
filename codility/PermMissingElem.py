def solution(A):
    A.sort()
    ans = 1
    for i in range(len(A)):
        if ans != A[i]:
            return ans
        else:
            ans += 1
    return ans