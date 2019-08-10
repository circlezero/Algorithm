import sys
n = int(sys.stdin.readline())

for i in range(n):
    s = '* '*(n)
    if i % 2 != 0:
        print(' '+s)
    else:
        print(s)