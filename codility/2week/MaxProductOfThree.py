def solution(A):
    A.sort(reverse=True)
    N = len(A)-1
    ans = A[0] * A[1] * A[2]
    if A[N] * A[N-1] > A[1] * A[2] and A[0] > 0:
        ans = A[0] * A[N] * A[N-1]
    return ans