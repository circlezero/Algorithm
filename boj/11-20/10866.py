import sys
import collections
input = sys.stdin.readline
n = int(input())
dq = collections.deque()

for i in range(n):
    op = input().strip()

    if op == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif op == 'back':
        if dq:
            print(dq[len(dq)-1])
        else:
            print(-1)
    elif op == 'size':
        print(len(dq))
    elif op == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif op == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif op == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)

    else:
        op, val = op.split()
        if op == 'push_front':
            dq.appendleft(val)
        elif op == 'push_back':
            dq.append(val)
