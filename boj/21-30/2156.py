import sys
input = sys.stdin.readline
n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))

d = [[0 for i in range(3)] for i in range(n+1)]
d[1][1] = a[1]
d[1][2] = a[1]
for i in range(2, n+1):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = d[i-1][0] + a[i]
    d[i][2] = d[i-1][1] + a[i]

print(max(d[n]))
