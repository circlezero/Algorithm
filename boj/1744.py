import sys
n = int(sys.stdin.readline())
a = []
zero = []
one = []
gtOne = []
ltZero = []

for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort(reverse=True)

for i in a:
    if i > 1:
        gtOne.append(i)
    elif i < 0:
        ltZero.append(i)
    elif i == 1:
        one.append(i)
    elif i == 0:
        zero.append(i)

ans = 0
tmp = 0
for i in gtOne:
    if tmp == 0:
        tmp = i
    else:
        ans += (tmp * i)
        tmp = 0
ans += tmp
tmp = 0
ans += sum(one)

ltZero.sort()
for i in ltZero:
    if tmp == 0:
        tmp = i
    else:
        ans += (tmp * i)
        tmp = 0

if len(zero) != 0:
    tmp = 0
ans += tmp
print(ans)