import sys
n, m, k = map(int, sys.stdin.readline().split())
ans = 0
while n >= 2 and m >= 1 and m + n >= k + 3:
    ans += 1
    n -= 2
    m -= 1
print(ans)