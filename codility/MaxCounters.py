import sys
A = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())

ans = [0 for i in range(N)]
maxCounter = 0
for i in A:
    if i == N + 1:
        ans = [maxCounter for i in range(N)]
    else:
        ans[i-1] += 1
        if maxCounter < ans[i-1]:
            maxCounter = ans[i-1]

print(ans)