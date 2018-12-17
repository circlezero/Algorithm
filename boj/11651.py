import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    a.append((y,x))

a.sort()
for i in a:
    print(f'{i[1]} {i[0]}')