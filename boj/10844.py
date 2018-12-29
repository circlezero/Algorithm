n = int(input())
d = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j-1 >= 0:
            d[i][j] += d[i-1][j-1]
        if j+1 <= 9:
            d[i][j] += d[i-1][j+1]

res = 0
for i in range(10):
    res += d[n][i]
res %= 1000000000
print(res)