import sys

n = int(sys.stdin.readline())
a = []
d = [[0 for i in range(3)] for i in range(n+1)]
for i in range(n):
    a.append(int(sys.stdin.readline()))

for i in range(1, n+1):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = d[i-1][0] + a[i-1]
    d[i][2] = d[i-1][1] + a[i-1]

print(max(d[i][0], d[i][1], d[i][2]))
            