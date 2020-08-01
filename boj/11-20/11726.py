import sys
n = int(sys.stdin.readline())
d = [1] * 1001

for i in range(2, n+1):
    d[i] = (d[i-1] + d[i-2]) % 10_007

print(d[n])
