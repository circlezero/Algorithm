def solution(A):
    N = len(A)
    ans = int(10E8 + 10E8)
    A.sort()
    front, back = 0, N - 1

    while front <= back:
        AbsSum = abs(A[front] + A[back])
        ans = min(AbsSum, ans)    
        if abs(A[front]) > abs(A[back]):
            front += 1
        else:
            back -= 1
    return ans

# print(solution([1000000000]))
print(solution([-8, 4, 5, -10, 3] ))