t = int(input())
a = [ [0 for x in range(15) ] for y in range(15) ]
for i in range(15):
    a[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, j+1):
            a[i][j] += a[i-1][k]

for i in range(t):
    k = int(input())
    n = int(input())
    print(a[k][n])