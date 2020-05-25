import sys
n = int(sys.stdin.readline())
d = [[0 for i in range(10)] for j in range(n+1)]

for i in range(10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(10):
            if j + k > 9:
                break
            d[i][j] += d[i-1][j+k]
        d[i][j] %= 10007

res = 0
for i in range(10):
    res += d[n][i]
res %= 10007

print(res)
