import sys
input = sys.stdin.readline
n, m = map(int, input().split())
na = list(map(int, input().split()))
ma = list(map(int, input().split()))
res = na + ma
res.sort()
for i in res:
    print(i, end=' ')
