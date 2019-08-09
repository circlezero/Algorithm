def solution(A, B):
    max_A = max(A)
    max_B = max(B)
    fibo = [0,1,2] + [0] * max_A
    for i in range(3, max_A + 1):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % (2**max_B)
    ans = []
    for i in range(len(A)):
        cnt = fibo[A[i]]
        ans.append( cnt % (2**B[i]) )
    return ans

print(solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]))