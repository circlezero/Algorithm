import sys

MAP = []
bingo = [0 for i in range(26)]
chkMap = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    MAP.append(list(map(int, sys.stdin.readline().split())))

for i in range(5):
    for j in range(5):
        bingo[MAP[i][j]] = (i, j)

speakNum = []
for i in range(5):
    speakNum.append(list(map(int, sys.stdin.readline().split())))

def chkFillLine(x, y):
    chkMap[x][y] = 1
    fillLine = 0

    # 가로 검사
    for i in range(5):
        flag = True
        for j in range(5):
            if chkMap[i][j] == 0:
                flag = False
                break
        if flag:
            fillLine += 1

    # 세로 검사
    for i in range(5):
        flag = True
        for j in range(5):
            if chkMap[j][i] == 0:
                flag = False
                break
        if flag:
            fillLine += 1
    
    # 대각선 검사
    flag = True
    for i in range(5):
        if chkMap[i][i] == 0:
            flag = False
            break
    if flag:
        fillLine += 1


    flag = True
    for i in range(5):
        if chkMap[i][4-i] == 0:
            flag = False
            break
    if flag:
        fillLine += 1
    
    return fillLine

res = 0
lineNum = 0
for i in speakNum:
    for j in i:
        x,y = bingo[j]
        if chkMap[x][y] == 0:
            lineNum = chkFillLine(x, y)
            res += 1
        if lineNum >= 3:
            break
    if lineNum >= 3:
            break
print(res)