import sys
res = ''
n = list(map(int, sys.stdin.readline().strip()))
n.sort(reverse=True)
for i in n:
    res += str(i)
res = int(res)

if res % 30 != 0:
    res = -1
print(res)