n = int(input())
d = [[0 for i in range(2)] for j in range(n+1)]

d[1][1] = 1
for i in range(2, n+1):
    for j in range(2):
        if j == 0:
            d[i][j] = d[i-1][1] + d[i-1][0]
        else:
            d[i][j] = d[i-1][0]

res = d[n][0] + d[n][1]
print(res)