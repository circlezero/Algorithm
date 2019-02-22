import sys
import queue

n = int(sys.stdin.readline())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
MAP = []
for i in range(n):
    arr = []
    for j in sys.stdin.readline().strip():
        arr.append(int(j))
    MAP.append(arr)

check = [[0 for i in range(n)] for j in range(n)]
def bfs(x, y):
    q = queue.Queue()
    q.put((x, y))
    res = 0

    while q.empty() != True:
        fx, fy = q.get()
        
        check[fx][fy] = 1
        res += 1
        
        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]
            if nx >= 0 and nx < n and \
                ny >= 0 and ny < n and \
                check[nx][ny] == 0 and MAP[nx][ny] == 1:
                q.put((nx, ny))
                check[nx][ny] = 1

    return str(res)
        
res = []
cnt = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and MAP[i][j] == 1:
          cnt += 1
          res.append(bfs(i, j))
res.sort()

print(cnt)
print('\n'.join(res))