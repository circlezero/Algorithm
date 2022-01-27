import sys
n = int(sys.stdin.readline())
d = [0] + [1] * 90

for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
