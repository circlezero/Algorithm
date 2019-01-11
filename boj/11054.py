import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [1] * 1001
d2 = [1] * 1001

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
        if a[n-i-1] > a[n-j-1] and d2[n-i-1] < d2[n-j-1] + 1:
            d2[n-i-1] = d2[n-j-1] + 1

maxLen = 0
for i in range(n):
    if maxLen < (d[i] + d2[i]):
        maxLen = (d[i] + d2[i])
print(maxLen - 1)