import sys
n = int(sys.stdin.readline())
d = [[0 for i in range(10)] for i in range(n+1)]
MOD = 1_000_000_000

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j + 1 < 10:
            d[i][j] += d[i-1][j+1]
        if j - 1 >= 0:
            d[i][j] += d[i-1][j-1]
        d[i][j] = d[i][j] % MOD


res = 0
for i in range(10):
    res = (res + d[n][i]) % MOD

print(res)
