import sys
input = sys.stdin.readline
n = int(input())
a = [[] for i in range(n)]
res = [0, 0, 0]

for i in range(n):
    a[i] = list(map(int, input().split()))


def isSame(x, y, s):
    for i in range(x, x+s):
        for j in range(y, y+s):
            if a[x][y] != a[i][j]:
                return False
    return True


def calcCnt(x, y):
    if a[x][y] == 1:
        res[2] += 1
    elif a[x][y] == 0:
        res[1] += 1
    elif a[x][y] == -1:
        res[0] += 1


def checkPaper(x, y, size):
    if size == 1:
        calcCnt(x, y)
        return

    if isSame(x, y, size):
        calcCnt(x, y)
    else:
        sm = size // 3
        checkPaper(x, y, sm)
        checkPaper(x, y+sm, sm)
        checkPaper(x, y+sm*2, sm)
        checkPaper(x+sm, y, sm)
        checkPaper(x+sm, y+sm, sm)
        checkPaper(x+sm, y+sm*2, sm)
        checkPaper(x+sm*2, y, sm)
        checkPaper(x+sm*2, y+sm, sm)
        checkPaper(x+sm*2, y+sm*2, sm)


checkPaper(0, 0, n)

for i in res:
    print(i)
