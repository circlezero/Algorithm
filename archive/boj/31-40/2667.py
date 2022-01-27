import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append(input().strip())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
check = [[False for i in range(25)] for i in range(25)]
danji = []


def bfs(x, y):
    num = 1
    check[x][y] = True
    dq = deque()
    dq.appendleft((x, y))

    while dq:
        tx, ty = dq.pop()

        for i in range(4):
            nx = dx[i] + tx
            ny = dy[i] + ty

            if (nx >= 0 and nx < n) and (ny >= 0 and ny < n) and a[nx][ny] == '1' and check[nx][ny] is False:
                dq.appendleft((nx, ny))
                check[nx][ny] = True
                num += 1

    return num


cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == '1' and check[i][j] is False:
            danji.append(bfs(i, j))
            cnt += 1
danji.sort()
print(cnt)
for i in danji:
    print(i)
