import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
check = [[False for i in range(m+1)] for i in range(n+1)]
dist = [[1 for i in range(m+1)] for i in range(n+1)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

a = []
for i in range(n):
    a.append(input().strip())


def bfs(x, y):
    dq = deque()
    dq.appendleft((x, y))

    while dq:
        tx, ty = dq.pop()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n and check[ny][nx] is False and a[ny][nx] == '1':
                dq.appendleft((nx, ny))
                check[ny][nx] = True
                dist[ny][nx] = dist[ty][tx] + 1


bfs(0, 0)
print(dist[n-1][m-1])
