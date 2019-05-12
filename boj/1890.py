import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

d = [[0 for i in range(n)] for j in range(n)]
d[0][0] = 1
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            break
        ni = i + a[i][j]
        nj = j + a[i][j]
        if ni < n:
            d[ni][j] += d[i][j]
        if nj < n:
            d[i][nj] += d[i][j]

print(d[n-1][n-1])