def solution(A, B):
    N = len(A)
    ans = 0
    segments = []
    for i in range(N):
        segments.append((B[i], A[i]))
    segments.sort()

    prev_end = -1
    for i in segments:
        curr_end, curr_start  = i
        if curr_start > prev_end:
            ans += 1
            prev_end = curr_end
    return ans

print(solution([0], [0]))
print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))
