import sys

def solution(A):
    N = max(A)
    L = len(A)
    M = [L] * (N+1)
    cnt = [0] * (N+1)

    for i in A:
        cnt[i] += 1

    for i in list(set(A)):
        j = i
        while j <= N:
            M[j] -= cnt[i]
            j += i

    ans = []
    for i in A:
        ans.append(M[i])
    return ans
        
print(solution([3, 1, 2, 3, 6]))
