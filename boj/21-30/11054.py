import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
p = [1] * n
m = [1] * n
d = [0] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i] and p[i] < p[j] + 1:
            p[i] = p[j] + 1

        if a[n-i-1] > a[n-j-1] and m[n-i-1] < m[n-j-1] + 1:
            m[n-i-1] = m[n-j-1] + 1

for i in range(n):
    d[i] = p[i] + m[i] - 1

print(max(d))
