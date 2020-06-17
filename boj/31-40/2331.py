import sys
input = sys.stdin.readline

A, P = map(int, input().split())
a = []
res = A
while res not in a:
    a.append(res)
    t = res
    res = 0
    for i in str(t):
        num = int(i) ** P
        res += num
print(a.index(res))
