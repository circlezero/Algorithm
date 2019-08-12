import sys
n = int(sys.stdin.readline())
i = 1
s = ['*']
L = 1

while i != n:
    L += 4
    p1 = '*' * L
    p2 = '*' + ' '*(L-2) + '*'
    prev = []
    for line in s:
        prev.append(f'* {line} *')
    s = [p1, p2] + prev + [p2, p1]
    i += 1

for i in s:
    print(i)