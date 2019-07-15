import sys
n = int(sys.stdin.readline())
ans = 0
if n % 4 == 0:
    ans = 1
    if n % 100 == 0:
        ans = 0
    if n % 400 == 0:
        ans = 1
print(ans)