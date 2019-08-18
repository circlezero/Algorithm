def solution(N):
    i = 1
    cnt = 0
    while i*i <= N:
        if N % i == 0:
            if i*i == N:
                cnt += 1
            else:
                cnt += 2
        i += 1
    return cnt

print(solution(24))