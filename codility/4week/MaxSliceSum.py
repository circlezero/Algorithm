def solution(A):
    N = len(A)
    acc_sum = 0
    max_sum = int(-10E5)
    for i in range(N):
        acc_sum += A[i]
        if max_sum < acc_sum:
            max_sum = acc_sum
        
        if max_sum < A[i]:
            max_sum = A[i]
            acc_sum = A[i]
        
        if acc_sum < A[i]:
            acc_sum = A[i]
        # print('A[i] :', A[i], 'acc_sum :', acc_sum, 'max_sum :', max_sum)
    return max_sum