import sys
a = list(map(int, sys.stdin.readline().split()))
ans = 0
eastCarCnt = 0
MAX = 1000000000

for i in a:
    if i == 0:
        eastCarCnt += 1
    else:
        ans += eastCarCnt

if ans > MAX:
    ans = -1
print(ans)