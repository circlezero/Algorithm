def solution(K, A):
    N = len(A)
    ans = 0
    tie = 0
    for i in range(N):
        tie += A[i]
        if tie >= K:
            ans += 1
            tie = 0
    return ans

print(solution(4, [1,2,3,4,1,1,3]))