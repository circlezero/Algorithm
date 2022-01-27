import sys
input = sys.stdin.readline
n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))

d = [[0 for i in range(3)] for j in range(n+1)]
d[1][1] = a[1]

for i in range(2, n+1):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + a[i]
    d[i][2] = d[i-1][1] + a[i]

print(max(d[n][1], d[n][2]))
