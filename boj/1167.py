import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[] for j in range(n+1)]
dist = [-1 for i in range(n+1)]

for i in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(s)-1, 2):
        a[s[0]].append((s[j], s[j+1]))

def BFS(num):
    dist = [-1 for i in range(n+1)]
    dist[num] = 0

    q = deque()
    q.appendleft(num)

    resNode = num
    resDist = 0
    
    while len(q) != 0:
        fn = q.pop()

        for i in a[fn]:
            nt, nd = i

            if nd != -1 and dist[nt] == -1:
                q.appendleft(nt)
                dist[nt] = dist[fn] + nd

                if dist[nt] > resDist:
                    resDist = dist[nt]
                    resNode = nt

    return (resNode, resDist)

node, dist = BFS(1)
resNode, resDist = BFS(node)
print(resDist)