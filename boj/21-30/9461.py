import sys
input = sys.stdin.readline

t = int(input())
d = [0, 1, 1, 1] + [0] * 100

for i in range(4, 101):
    d[i] = d[i-2] + d[i-3]

for i in range(t):
    n = int(input())
    print(d[n])
