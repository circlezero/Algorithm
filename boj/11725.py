import sys
from collections import deque

n = int(sys.stdin.readline())
node = [[] for i in range(n+1)]
chkNode = [0]
parent = [0 for i in range(n+1)]

for i in range(1, n):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

q = deque()
q.appendleft(1)

while len(q) != 0:
    f = q.pop()

    for i in node[f]:
        if parent[i-1] == 0:
            q.appendleft(i)
            parent[i-1] = f

for i in range(1, n):
    print(parent[i])