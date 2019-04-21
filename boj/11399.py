import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

ans = 0
watingTime = 0
for i in a:
    watingTime += i
    ans += watingTime

print(ans)