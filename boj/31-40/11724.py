import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False for i in range(n+1)]
a = [[] for i in range(n+1)]


def bfs(x):
    dq = deque()
    dq.append(x)
    visited[x] = True

    while dq:
        y = dq.popleft()
        for i in a[y]:
            if visited[i] is False:
                dq.append(i)
                visited[i] = True


for i in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

res = 0
for i in range(1, n+1):
    if visited[i] is True:
        continue

    bfs(i)
    res += 1

print(res)
