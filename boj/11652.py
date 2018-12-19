import sys
n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()

cntMax = 1
cnt = 0

cntNum = a[0]
current = a[0]

for i in a:
    if current == i:
        cnt += 1
    else:
        if cnt > cntMax:
            cntMax = cnt
            cntNum = current
        current = i
        cnt = 1

if cnt > cntMax:
    cntMax = cnt
    cntNum = current

print(cntNum)