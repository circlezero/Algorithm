import sys
A = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
ans = [0] * N

maxCounter = 0
curMax = 0

for i in A:
    if i == N + 1:
        maxCounter = curMax
    else:
        if ans[i-1] < maxCounter:
            ans[i-1] = maxCounter
        ans[i-1] += 1
        if ans[i-1] > curMax:
            curMax = ans[i-1]

for i in range(N):
    if ans[i] < maxCounter:
        ans[i] = maxCounter
print(ans)