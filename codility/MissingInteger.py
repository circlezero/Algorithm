import sys
a = list(map(int, sys.stdin.readline().split()))
a.sort()
ans = 1
for i in a:
    if i == ans:
        ans += 1
print(ans)