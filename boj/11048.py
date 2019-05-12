import sys
n, m = map(int ,sys.stdin.readline().split())
d = [[0 for i in range(m+1)] for j in range(n+1)]
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

d[0][0] = a[0][0]
for i in range(1, m):
    d[0][i] = d[0][i-1] + a[0][i]

for i in range(1, n):
    d[i][0] = d[i-1][0] + a[i][0]

for i in range(1, n):
    for j in range(1, m):
        d[i][j] = max(d[i-1][j], d[i][j-1]) + a[i][j]
print(d[n-1][m-1])