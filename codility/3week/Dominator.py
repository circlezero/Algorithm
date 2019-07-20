from collections import Counter
def solution(A):
    if not A:
        return -1

    D = Counter(A).most_common(1)[0]
    if (len(A) // 2) >= D[1]:
        return -1
    return A.index(D[0])