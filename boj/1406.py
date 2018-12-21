import sys
sl = list(sys.stdin.readline().strip())
sr = []
n = int(sys.stdin.readline())

for i in range(n):
    op = sys.stdin.readline().strip()
    if op == 'L':
        if len(sl) < 1:
            continue
        sr.append(sl.pop())
    elif op == 'D':
        if len(sr) < 1:
            continue
        sl.append(sr.pop())
    elif op == 'B':
        if len(sl) < 1:
            continue
        sl.pop()
    else:
        op, plus = op.split()
        sl.append(plus)

for i in range(len(sr)):
    sl.append(sr.pop())
print(''.join(sl))