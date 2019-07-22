from collections import Counter
def solution(A):
    ans = 0
    if not A:
        return ans
    left = Counter()
    right = Counter(A)
    left_val, left_cnt = 0, 0
    for i in range(len(A)-1):
        left[A[i]] += 1
        right[A[i]] -= 1
        if left_cnt < left[A[i]]:
            left_cnt = left[A[i]]
            left_val = A[i]
        if ((i+1) // 2) < left_cnt and ((len(A)-i-1) // 2) < right[left_val]:
            ans += 1
    return ans

print(solution([4,3,4,4,4,2]))