import sys
s = sys.stdin.readline()
n = len(s)
s = " " + s
d = [0 for i in range(n+1)]
c = [[False for i in range(n+1)] for j in range(n+1)]

for i in range(1, n+1):
    c[i][i] = True
for i in range(1, n):
    if s[i] == s[i+1]:
        c[i][i+1] = True
for k in range(2, n):
    for i in range(1, n-k+1):
        j = i+k-1
        if s[i] == s[j] and c[i+1][j-1]:
            c[i][j] = True

for i in range(1, n):
    d[i] = -1
    for j in range(1, i+1):
        if c[j][i]:
            if d[i] == -1 or d[i] > d[j-1] + 1:
                d[i] = d[j-1] + 1

print(d[n-1])