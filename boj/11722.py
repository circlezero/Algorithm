import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [1] * 1001

for i in range(n):
    for j in range(i):
        if a[i] < a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

maxLen = 0
for i in range(n):
    if maxLen < d[i]:
        maxLen = d[i]
print(maxLen)