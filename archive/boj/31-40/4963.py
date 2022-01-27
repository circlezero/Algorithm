import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
check = [[False for i in range(51)] for i in range(51)]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    check = [[False for i in range(w+1)] for i in range(h+1)]

    cnt = 0

    def bfs(x, y):
        dq = deque()
        dq.appendleft((x, y))
        check[y][x] = True

        while dq:
            tx, ty = dq.pop()
            for i in range(8):
                nx = tx + dx[i]
                ny = ty + dy[i]

                if (nx >= 0 and nx < w) \
                        and (ny >= 0 and ny < h) \
                        and check[ny][nx] is False \
                        and a[ny][nx] == 1:
                    dq.appendleft((nx, ny))
                    check[ny][nx] = True

    for i in range(h):
        for j in range(w):
            if a[i][j] == 1 and check[i][j] is False:
                bfs(j, i)
                cnt += 1

    print(cnt)
