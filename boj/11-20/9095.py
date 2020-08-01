import sys
input = sys.stdin.readline
n = int(input())
d = [1, 1, 2] + [1] * 10

for i in range(3, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in range(n):
    t = int(input())
    print(d[t])
