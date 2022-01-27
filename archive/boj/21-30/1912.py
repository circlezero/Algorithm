import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [0] * n

for i in range(n):
    d[i] = a[i]

for i in range(1, n):
    if d[i-1] + a[i] < a[i]:
        d[i] = a[i]
    else:
        d[i] = d[i-1] + a[i]

print(max(d))
