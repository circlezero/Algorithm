import sys
a, b, k = list(map(int, sys.stdin.readline().split()))
ans = (b // k) - (a // k)
if (a % k == 0):
    ans += 1
print(ans) 