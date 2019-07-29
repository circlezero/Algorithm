import sys
n = int(sys.stdin.readline())

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(1, 2*(n - i)):
        print('*', end='')
    print()