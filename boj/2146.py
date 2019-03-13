import sys
from collections import deque

n = int(sys.stdin.readline())

imap = []
gmap = [[0 for i in range(n)] for j in range(n)]
dmap = [[-1 for i in range(n)] for j in range(n)]
chkMap = [[0 for i in range(n)] for j in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    imap.append(list(map(int, sys.stdin.readline().split())))

# 섬의 숫자를 입력하는 함수
def IslandNum(x, y, num):
    q = deque()
    q.append((x,y))
    gmap[y][x] = num

    while len(q) != 0:
        fx, fy = q.pop()

        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]

            if (nx >= 0 and nx < n) and (ny >= 0 and ny < n) and imap[ny][nx] == 1 and gmap[ny][nx] == 0:
                q.append((nx, ny))
                gmap[ny][nx] = num

# BFS 한 단계만 진행하는 함수
def BFSOneStep():

                
# 처음 섬이 있는 곳은 거리가 0 & 섬의 숫자 매기기
iNum = 1
for i in range(n):
    for j in range(n):
        if imap[i][j] == 1:
            dmap[i][j] = 0
        
        if imap[i][j] == 1 and gmap[i][j] == 0:
            IslandNum(j, i, iNum)
            iNum += 1


        
print('-------')
# for i in imap:
#     print(i)

# for i in gmap:
#     print(i)

# for i in dmap:
#     print(i)