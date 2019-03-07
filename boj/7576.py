import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

q = deque()
m, n = map(int, sys.stdin.readline().split())
tmap = []
chkTomato = [[-1 for i in range(m)] for j in range(n)]
res = 0
        
for i in range(n):
    tmap.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if tmap[i][j] == 1:
            q.appendleft((j, i))
            chkTomato[i][j] = 0

while len(q) != 0:
    fx, fy = q.pop()
    
    for i in range(4):
        nx = fx + dx[i]
        ny = fy + dy[i]

        if (nx >= 0 and nx < m) and \
            (ny >= 0 and ny < n) and \
            chkTomato[ny][nx] == -1 and tmap[ny][nx] != -1:
            q.appendleft((nx, ny))
            chkTomato[ny][nx] = chkTomato[fy][fx] + 1
            if res < chkTomato[ny][nx]:
                res = chkTomato[ny][nx]

for i in range(n):
    for j in range(m):
        if chkTomato[i][j] == -1 and tmap[i][j] == 0:
            res = -1

print(res)