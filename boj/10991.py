import sys
n = int(sys.stdin.readline())

for i in range(n):
    print(' '*(n-i-1), end='')
    for j in range(i+1):
        print('*', end=' ')
    print()