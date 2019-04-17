import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[] for i in range(n+1)]
dist = [-1 for i in range(n+1)]

for i in range(1, n):
    parent, child, value = map(int, sys.stdin.readline().split())
    a[parent].append((child, value))

def BFS(num):
    dist = [-1 for i in range(n+1)]
    dist[num] = 0

    q = deque()
    q.appendleft(num)

    resDist = 0
    resNode = num

    while len(q) != 0:
        fn = q.pop()

        for i in a[fn]:
            nodeTo, nodeDist = i
            if nodeDist != -1 and dist[nodeTo] == -1:
                q.appendleft(nodeTo)
                dist[nodeTo] = dist[fn] + nodeDist

                if dist[nodeTo] > resDist:
                    resDist = dist[nodeTo]
                    resNode = nodeTo
    
    return (resNode, resDist)

resNode, resDist = BFS(1)
print(resNode, resDist)
resNode, resDist = BFS(resNode)
print(resNode, resDist)
print(resDist)