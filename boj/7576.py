import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

m, n = map(int, sys.stdin.readline().split())
tmap = []
chkTomato = [[-1 for i in range(m)] for j in range(n)]

def bfs(x, y):
    q = deque()
    q.appendleft((x,y))
    chkTomato[y][x] = 1

    while len(q) != 0:
        fx, fy = q.pop()

        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]

            if (nx >= 0 and nx < m) and \
                (ny >= 0 and ny < n) and \
                tmap[ny][nx] != -1:
                q.appendleft((nx, ny))

                

                chkTomato[ny][nx] = chkTomato[fy][fx] + 1
                if chkTomato[ny][nx] > chkTomato[fy][fx] + 1:
                    chkTomato[ny][nx] = chkTomato[fy][fx] + 1
                elif chkTomato[ny][nx] != -1
                
                chkTomato[ny][nx] < chkTomato[fy][fx] + 1 and \
                
                
            
for i in range(n):
    tmap.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if tmap[i][j] == 1:
            bfs(j, i)

for i in range(n):
    print(chkTomato[i])