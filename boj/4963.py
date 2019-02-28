import sys
from collections import deque

dx = [1, 1, 0, -1, -1, -1, 0, 1 ]
dy = [0, -1, -1, -1, 0, 1, 1, 1 ]
chkMap = [[0 for i in range(51)] for j in range(51)]

def bfs(x, y, w, h):
    q = deque()
    q.appendleft((x, y))
    chkMap[y][x] = 1

    while len(q) != 0:
        fx, fy = q.pop()

        for i in range(8):
            nx = fx + dx[i]
            ny = fy + dy[i]

            if (nx >= 0 and nx < w) and\
                (ny >= 0 and ny < h) and\
                chkMap[ny][nx] == 0 and MAP[ny][nx] == 1:
                q.appendleft((nx, ny))
                chkMap[ny][nx] = 1



while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    else:
        MAP = []
        chkMap = [[0 for i in range(51)] for j in range(51)]
        cntIsland = 0
        for i in range(h):
            MAP.append(list(map(int, sys.stdin.readline().split())))
        
        for i in range(h):
            for j in range(w):
                if chkMap[i][j] == 0 and MAP[i][j] == 1:
                    cntIsland += 1
                    bfs(j, i, w, h)

        print(cntIsland)