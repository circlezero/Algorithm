import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

c = [[0 for i in range(n)] for i in range(n)]
dist = [[0 for i in range(n)] for i in range(n)]
dq = deque()


def bfs(x, y, num):
    dq.appendleft((x, y))
    c[y][x] = num

    while dq:
        tx, ty = dq.pop()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and \
                    a[ny][nx] == 1 and c[ny][nx] == 0:
                dq.appendleft((nx, ny))
                c[ny][nx] = num


cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and c[i][j] == 0:
            cnt += 1
            bfs(j, i, cnt)

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            dq.appendleft((j, i))

while dq:
    tx, ty = dq.pop()

    for i in range(4):
        nx = tx + dx[i]
        ny = ty + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if c[ny][nx] == 0 and dist[ny][nx] == 0:
                dq.appendleft((nx, ny))
                dist[ny][nx] = dist[ty][tx] + 1
                c[ny][nx] = c[ty][tx]

res = n ** 2
for y in range(n):
    for x in range(n):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and \
                    c[ny][nx] != c[y][x] and res > (dist[ny][nx] + dist[y][x]):
                res = dist[ny][nx] + dist[y][x]
print(res)
