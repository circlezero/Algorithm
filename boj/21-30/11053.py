import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

res = [a[0]]
for i in range(1, n):
    if a[i] > max(res):
        res.append(a[i])
