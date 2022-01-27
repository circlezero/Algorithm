import sys
input = sys.stdin.readline
sl = list(input().strip())
sr = []
m = int(input())

for i in range(m):
    op = input().strip()
    if op == 'L':
        if sl:
            sr.append(sl.pop())
    elif op == 'D':
        if sr:
            sl.append(sr.pop())
    elif op == 'B':
        if sl:
            sl.pop()
    else:
        _, var = op.split()
        sl.append(var)

for i in range(len(sr)):
    sl.append(sr.pop())
print(''.join(sl))
