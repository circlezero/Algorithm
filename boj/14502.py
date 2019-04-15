import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
MAP = []
for i in range(n):
    MAP.append(list(map(int, sys.stdin.readline().split())))

vMap = [[0 for i in range(9)] for j in range(9)]
tMap = [[0 for i in range(9)] for j in range(9)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
q = deque()
ans = 0

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 2:
            q.appendleft((i, j))

def spreadVirus():
    global ans
    vMap = copy.deepcopy(tMap)
    nq = deque(q)
    while len(nq) != 0:
        fy, fx = nq.pop()

        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]

            if (nx >= 0 and nx < m) and (ny >= 0 and ny < n) and vMap[ny][nx] == 0:
                vMap[ny][nx] = 2
                nq.appendleft((ny, nx))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if vMap[i][j] == 0:
                cnt += 1
    ans = max(cnt, ans)

def wall(cnt):
    if cnt == 3:
        spreadVirus()
        return
    else:
        for i in range(n):
            for j in range(m):
                tMap[i][j] = 1
                wall(cnt + 1)
                tMap[i][j] = 0

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 0:
            tMap = copy.deepcopy(MAP)
            tMap[i][j] = 1
            wall(1)
            tMap[i][j] = 0

print(ans)
