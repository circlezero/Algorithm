import sys
from collections import deque

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

# 처음 상어 위치
babySharkPosition = (0, 0)
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            babySharkPosition = (j, i)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
babyShark = 2

# 물고기 찾아서 (y 좌표, x 좌표, 거리) 반환 하는 함수
def FishSearch(x, y):
    distMap = [[-1 for i in range(n)] for j in range(n)]
    distMap[y][x] = 0

    q = deque()
    q.appendleft((x, y))
    d = 0

    fish = []
    while len(q) != 0:
        fx, fy = q.pop()
        if d < distMap[fy][fx]:
            d = distMap[fy][fx]
            if len(fish) != 0:
                fish.sort()
                return fish[0]

        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]

            if (nx >= 0 and nx < n) and (ny >= 0 and ny < n) and distMap[ny][nx] == -1 and a[ny][nx] <= babyShark:
                dist = distMap[fy][fx] + 1
                distMap[ny][nx] = dist
                q.appendleft((nx, ny))
                if a[ny][nx] != 0 and a[ny][nx] < babyShark:
                    fish.append((dist, ny, nx))

    return (0, -1, -1)

ans = 0
eatCnt = 0
while True:
    x, y = babySharkPosition
    dist, targetY, targetX = FishSearch(x, y)
    
    
    if targetX == -1 and targetY == -1:
        break

    ans += dist
    babySharkPosition = (targetX, targetY)
    a[y][x] = 0
    eatCnt += 1

    if eatCnt == babyShark:
        babyShark += 1
        eatCnt = 0

print(ans)