import sys
input = sys.stdin.readline
n, m = map(int, input().split())
c = list(map(int, input().split()))
c.sort(reverse=True)
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tSum = c[i] + c[j] + c[k]
            if ans < tSum <= m:
                ans = tSum
print(ans)