import sys
n = int(sys.stdin.readline())
a = [[0 for i in range(n+1)] for j in range(n+1)]
num = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n):
    b = list(map(int, sys.stdin.readline().split()))
    for j in range(len(b)):
        num[i][j] = b[j]

a[0][0] = num[0][0]
for i in range(n):
    for j in range(i+1):
        a[i+1][j] = max(a[i+1][j], num[i+1][j] + a[i][j])
        a[i+1][j+1] = max(a[i+1][j+1], num[i+1][j+1] + a[i][j])
print(max(a[n-1]))