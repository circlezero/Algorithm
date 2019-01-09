import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [1] * 1000

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
        
maxLen = 0
for i in range(n):
    if d[i] > maxLen:
        maxLen = d[i]
print(maxLen)