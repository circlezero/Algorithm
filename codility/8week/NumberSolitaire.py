def solution(A):
    N = len(A)
    D = [0] * (N + 1)
    D[0] = A[0]
    
    for i in range(1, N):
        B = []
        for j in range(1, 7):
            if i - j >= 0:
                B.append(D[i-j] + A[i])
        if B:
            D[i] = max(B)
    return D[N-1]

print(solution([1, -2, 0, 9, -1, -2]))
print(solution([4, -3]))