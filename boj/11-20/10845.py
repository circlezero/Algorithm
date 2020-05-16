import sys
import collections
input = sys.stdin.readline
q = collections.deque()
n = int(input())
for i in range(n):
    op = input().strip()
    if op == 'pop':
        if q:
            print(q.popleft())
        else:
            print('-1')

    elif op == 'size':
        print(len(q))

    elif op == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif op == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif op == 'back':
        if q:
            print(q[len(q)-1])
        else:
            print('-1')

    else:
        _, var = op.split()
        q.append(var)
