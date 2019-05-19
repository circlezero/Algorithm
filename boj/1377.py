import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append((int(sys.stdin.readline()), i))
a.sort()
ans = 0
for i in range(n):
    print(a[i][1], i)
    ans = max(ans, a[i][1] - i)
print(ans+1)