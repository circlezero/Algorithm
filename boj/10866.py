import sys
import collections

n = int(sys.stdin.readline())
d = collections.deque()
for i in range(n):
    op = sys.stdin.readline().strip()
    if op == 'front':
        if len(d) == 0:
            print('-1')
        else:    
            print(d[0])
    elif op == 'back':
        if len(d) == 0:
            print('-1')
        else:    
            print(d[len(d)-1])
    elif op == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif op == 'size':
        print(len(d))
    elif op == 'pop_front':
        if len(d) == 0:
            print('-1')
        else:
            print(d.popleft())
    elif op == 'pop_back':
        if len(d) == 0:
            print('-1')
        else:
            print(d.pop())
    else:
        op, num = op.split()
        if op == 'push_back':
            d.append(int(num))
        elif op == 'push_front':
            d.appendleft(int(num))