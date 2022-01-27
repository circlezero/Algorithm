import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())

a = [[0 for i in range(n+1)] for i in range(n+1)]
visited = [False for i in range(n+1)]
b = [[] for i in range(n+1)]


def dfs(x):
    print(x, end=" ")
    visited[x] = True
    for i in range(1, n+1):
        if visited[i] is False and a[x][i] == 1:
            dfs(i)


def bfs(x):
    visited = [False for i in range(n+1)]
    dq = deque()
    dq.append(x)
    visited[x] = True

    while dq:
        y = dq.popleft()
        print(y, end=' ')
        b[y].sort()
        for i in b[y]:
            if visited[i] is False:
                dq.append(i)
                visited[i] = True


for i in range(m):
    s, e = map(int, input().split())
    a[s][e] = a[e][s] = 1
    b[s].append(e)
    b[e].append(s)

dfs(v)
print()
bfs(v)
