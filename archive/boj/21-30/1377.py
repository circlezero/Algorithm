import sys
input = sys.stdin.readline

t = int(input())
a = []
for i in range(t):
    a.append((int(input()), i))
a.sort()

ans = 0
for i in range(t):
    ans = max(ans, a[i][1] - i)

print(ans+1)
