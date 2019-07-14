def chkTriangle(P, A):
    Q = P + 1
    R = Q + 1
    if A[P] + A[Q] <= A[R]:
        return False
    if A[R] + A[Q] <= A[P]:
        return False
    if A[R] + A[P] <= A[Q]:
        return False
    return True

def solution(A):
    A.sort()
    for i in range(len(A)-2):
        if chkTriangle(i, A):
            return 1
    return 0