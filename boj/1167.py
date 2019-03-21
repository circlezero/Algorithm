import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[-1 for i in range(n+1)] for j in range(n+1)]
dist = [-1 for i in range(n+1)]

for i in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(s)-1, 2):
        a[s[0]][s[j]] = s[j+1]

def BFS(num):
    dist[num] = 0
    q = deque()
    q.appendleft(num)

    resNode = 1
    resDist = 0
    
    while len(q) != 0:
        fn = q.pop()

        for i in range(1, n+1):
            fd = a[fn][i]
            if fd != -1 and dist[i] == -1:
                q.appendleft(i)
                dist[i] = dist[fn] + fd 
                if dist[i] > resDist:
                    resDist = dist[i]
                    resNode = i

    return (resNode, resDist)

dist = [-1 for i in range(n+1)]
node, dist = BFS(1)
dist = [-1 for i in range(n+1)]
resNode, resDist = BFS(node)
print(resDist)