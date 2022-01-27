import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
cost = [-1] * (n+1)
arr = [[] for i in range(n+1)]

for i in range(1, n):
    parent, child, cost = map(int, input().split())
    arr[parent].append((child, cost))
    arr[child].append((parent, cost))


def bfs(x):
    cost = [-1] * (n+1)
    cost[x] = 0

    dq = deque()
    dq.append(x)

    node = x
    res = 0

    while dq:
        fn = dq.pop()
        if res < cost[fn]:
            node = fn
            res = cost[fn]

        for i in arr[fn]:
            nn, nc = i

            if cost[nn] < 0 and nc != -1:
                dq.appendleft(nn)
                cost[nn] = cost[fn] + nc

    return (node, res)


node, _ = bfs(1)
_, res = bfs(node)

print(res)
