import sys
A = list(map(int, sys.stdin.readline().split()))
N = len(A)
ans = 0

def isIntersect(a, b):
    for i in range(b-A[b], b+A[b]+1):
        if a-A[a] <= i <= a+A[a]:
            return True
    return False

for i in range(N):
    for j in range(i+1, N):
        if isIntersect(i, j):
            ans += 1

if ans >= 10000000:
    ans = -1
print(ans)

