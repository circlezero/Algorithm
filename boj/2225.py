import sys
n, k = list(map(int, sys.stdin.readline().split()))
d = [[0 for i in range(201)] for i in range(201)]
d[0][0] = 1
mod = 1000000000
for i in range(1, k+1):
    for j in range(n+1):
        for h in range(j+1):
            d[i][j] += d[i-1][j-h]
            d[i][j] %= mod

print(d[k][n])