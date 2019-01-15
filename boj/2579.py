import sys
n = int(sys.stdin.readline())
d = [[0 for i in range(3)] for i in range(n)]
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

d[0][1] = a[0]
d[1][1] = a[1]
d[1][2] = a[0] + a[1]
for i in range(2, n):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + a[i]
    d[i][2] = d[i-1][1] + a[i]
print(max(d[n-1][1], d[n-1][2]))