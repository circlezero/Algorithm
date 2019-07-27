def solution(A):
    if not A:
        return 0
    
    max_profit = 0
    buy = A[0]
    N = len(A)

    for i in range(N):
        if A[i] < buy:
            buy = A[i]
        elif i != 0:
            continue

        for j in range(i+1, N):
            profit = A[j] - buy
            if profit > max_profit:
                max_profit = profit
    return max_profit

print(solution([0, 200000]))