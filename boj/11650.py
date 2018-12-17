import sys
a = []
n = int(sys.stdin.readline())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append((x,y))
a.sort()
for i in a:
    print(f'{i[0]} {i[1]}')