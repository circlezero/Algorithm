import sys
import queue

checked = [0] * 1001
n, m, v = list(map(int, sys.stdin.readline().split()))
connect = [[] for i in range(n+1)]
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    connect[a].append(b)
    connect[b].append(a)

for i in range(n+1):
    connect[i].sort()

def dfs(start):
    checked[start] = 1
    print(start, end=" ")

    for i in connect[start]:
        next = i
        if checked[next] == 0:
            dfs(next)


def bfs(start):
    q = queue.Queue()
    checked = [0] * 1001
    checked[start] = 1
    q.put(start)
    while q.empty() != True:
        f = q.get()
        print(f, end=" ")
        for i in connect[f]:
            next = i
            if checked[next] == 0:
                checked[next] = 1
                q.put(next)

dfs(v)
print()
bfs(v)
