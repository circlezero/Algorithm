import sys
input = sys.stdin.readline
res = 0
acc = 0
prev = -1
for i in input():
    if i == '(':
        acc += 1
        prev = 0
    elif i == ')':
        acc -= 1
        if prev == 0:
            res += acc
        else:
            res += 1
        prev = 1
print(res)
