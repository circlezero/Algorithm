import sys
n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
d = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n+1):
    d[i][i] = 1

for i in range(1, n):
    if a[i] == a[i+1]:
        d[i][i+1] = 1

for k in range(3, n+1):
    for i in range(1, n-k+2):
        j = i+k-1
        if a[i] == a[j] and d[i+1][j-1]:
            d[i][j] = 1

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(d[s][e])