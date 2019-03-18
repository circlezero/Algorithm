import sys
from collections import deque

n = int(sys.stdin.readline())
d = [[] for i in range(n+1)]
res = 0

for i in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(s)-1, 2):
        d[s[0]].append((s[j], s[j+1]))


def BFS(num):
    q.appendleft(num)
    check[num] = 1

    for i in d[num]:
        node, dist = i
        q.appendleft((node, dist))
        check[node] = 1

    while len(q) != 0:
        fn, fd = q.pop()
        for i in d[fn]:
            node, dist = i
            newDist = dist + fd
            if check[node] == 0:
                q.appendleft((node, newDist))

BFS(1)
start = 1

BFS(start)

print(res)