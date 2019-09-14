def solution(A):
    ans = []
    for i in range(len(A)):
        if A[i] < 0:
            ans.append(-A[i])
        else:
            ans.append(A[i])
    ans = list(set(ans))
    return len(ans)

print(solution([-5, -3, -1, 0, 3, 6]))