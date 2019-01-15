import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [0] * 100001

for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i-1] + a[i]:
        d[i] = d[i-1] + a[i]

maxSum = d[0]
for i in range(1, n):
    if maxSum < d[i]:
        maxSum = d[i]
print(maxSum)