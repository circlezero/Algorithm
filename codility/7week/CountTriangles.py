def solution(A):
    A.sort()
    N = len(A)
    ans = 0
    for P in range(N-2):
        Q = P + 1
        R = Q + 1
        while R < N:
            if A[P] + A[Q] > A[R]:
                ans += R - Q
                R += 1
            elif Q < R - 1:
                Q += 1
            else:
                Q += 1
                R += 1
    return ans

print(solution([10, 2, 5, 1, 8, 12]))