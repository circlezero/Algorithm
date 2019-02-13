import sys
import queue

n, m = list(map(int, sys.stdin.readline().split()))
checked = [False] * 1001
edge = [[] for i in range(1001)]
res = 0

def bfs(start):
    q = queue.Queue()
    q.put(start)
    checked[start] = True

    while q.empty() != True:
        first = q.get()
        for i in edge[first]:
            if checked[i] == False:
                q.put(i)
                checked[i] = True

for i in range(m):
    u, v = list(map(int, sys.stdin.readline().split()))
    edge[u].append(v)
    edge[v].append(u)

for i in range(1, n+1):
    if checked[i] == False:
        bfs(i)
        res += 1

print(res)