import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))
chkMap = [[0 for i in range(m)] for j in range(n)]
MAP = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    MAP.append(list(map(int, sys.stdin.readline().strip())))

def bfs(x, y):
    q = deque()
    q.appendleft((x,y))
    chkMap[y][x] = 1

    while len(q) != 0:
        fx, fy = q.pop()
        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]

            if (nx >= 0 and nx < m) and (ny >= 0 and ny < n) and \
                chkMap[ny][nx] == 0 and MAP[ny][nx] == 1:
                q.appendleft((nx, ny))
                chkMap[ny][nx] = chkMap[fy][fx] + 1

bfs(0,0)
print(chkMap[n-1][m-1])