import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
edge = [[] for i in range(n+1)]

for i in range(n):
    e = list(map(int, input().split()))
    node = e[0]
    for i in range(1, len(e)-1, 2):
        edge[node].append((e[i], e[i+1]))


def bfs(x):
    cost = [-1 for i in range(n+1)]
    check = [False for i in range(n+1)]
    cost[x] = 0

    dq = deque()
    dq.appendleft(x)

    resNode = x
    resDist = 0

    while dq:
        num = dq.pop()

        for i in edge[num]:
            node, price = i
            if price != -1 and cost[node] == -1:
                dq.appendleft(node)
                cost[node] = price + cost[num]
                if cost[node] > resDist:
                    resDist = cost[node]
                    resNode = node

    return (resNode, resDist)


N, D = bfs(1)
RN, RD = bfs(N)
print(RD)
