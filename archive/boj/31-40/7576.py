import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
c = [[False for i in range(m+1)] for i in range(n+1)]
dist = [[0 for i in range(m)] for i in range(n)]

a = []
for i in range(n):
    a.append(list(map(int, input().split())))


dq = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            dq.append((j, i))
            c[i][j] = True

while dq:
    tx, ty = dq.pop()

    for i in range(4):
        nx = tx + dx[i]
        ny = ty + dy[i]

        if (nx >= 0 and nx < m) and (ny >= 0 and ny < n) and \
                a[ny][nx] == 0 and c[ny][nx] is False:
            dist[ny][nx] = dist[ty][tx] + 1
            dq.appendleft((nx, ny))
            c[ny][nx] = True

res = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and c[i][j] == False:
            res = -1
            break

        if dist[i][j] > res:
            res = dist[i][j]
    if res < 0:
        break

print(res)
