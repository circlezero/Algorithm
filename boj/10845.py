import sys
import collections

n = int(sys.stdin.readline())
q = collections.deque()

for i in range(n):
    op = sys.stdin.readline().strip()
    if op == 'size':
        print(len(q))
    elif op == 'empty':
        if len(q) == 0:
            print('1')
        else:
            print('0')
    elif op == 'pop':
        if len(q) == 0:
            print('-1')
        else:
            print(q.popleft())
    elif op == 'front':
        if len(q) == 0:
            print('-1')
        else :
            print(q[0])
    elif op == 'back':
        if len(q) == 0:
            print('-1')
        else:
            print(q[len(q) - 1])
    else:
        op, num = op.split()
        q.append(num)