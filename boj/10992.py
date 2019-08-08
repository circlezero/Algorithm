import sys
n = int(sys.stdin.readline())

for i in range(n):
    if i == n-1:
        print('*'*(2*n-1))
    else:
        print(' '*(n-i-1), end='')
        print('*', end='')
        print(' '*(2*i-1), end='')
        if i != 0:
            print('*', end='')
        print()