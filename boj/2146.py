import sys
from collections import deque

n = int(sys.stdin.readline())

imap = []
gmap = [[0 for i in range(n)] for j in range(n)]
dmap = [[-1 for i in range(n)] for j in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    imap.append(list(map(int, sys.stdin.readline().split())))

def chkRange(x, y):
    if (x >= 0 and x < n) and (y >= 0 and y < n):
        return True
    else:
        return False

# 섬의 숫자를 입력하는 함수
def IslandNum(x, y, num):
    q = deque()
    q.appendleft((x,y))
    gmap[y][x] = num

    while len(q) != 0:
        fx, fy = q.pop()

        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]

            if chkRange(nx, ny) and imap[ny][nx] == 1 and gmap[ny][nx] == 0:
                q.appendleft((nx, ny))
                gmap[ny][nx] = num

# 처음 섬이 있는 곳은 거리가 0 & 섬의 그룹 넘버 매기기
iNum = 1
queue = deque()
for y in range(n):
    for x in range(n):
        if imap[y][x] == 1:
            queue.appendleft((x,y))
            dmap[y][x] = 0

            if gmap[y][x] == 0:
                IslandNum(x, y, iNum)
                iNum += 1
            

# dmap & gmap 나머지 공간 채우기
while len(queue) != 0:
    fx, fy = queue.pop()

    for i in range(4):
        nx = fx + dx[i]
        ny = fy + dy[i]

        if chkRange(nx, ny) and imap[ny][nx] == 0 and dmap[ny][nx] == -1 and gmap[ny][nx] == 0:
            queue.appendleft((nx, ny))
            dmap[ny][nx] = dmap[fy][fx] + 1
            gmap[ny][nx] = gmap[fy][fx]
            

# 인접한 블록에 다른 그룹넘버가 있으면 현재 거리 + 인접 블록의 거리로 다리를 건설
res = -1
for y in range(n):
    for x in range(n):

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if chkRange(nx, ny) and (gmap[y][x] != gmap[ny][nx]):
                if res == -1 or (res > (dmap[y][x] + dmap[ny][nx])):
                    res = dmap[y][x] + dmap[ny][nx]
print(res)

# print("[Group Map]                      |   [Dist Map]")
# for i in range(n):
#     print(gmap[i], end="   |   ")
#     print(dmap[i])

# print(f'result = {minLen}')