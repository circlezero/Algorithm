import sys
input = sys.stdin.readline
sys.setrecursionlimit(200002)

a = [[] for i in range(20002)]
colors = [0 for i in range(20002)]


def dfs(x, c):
    colors[x] = c
    for i in a[x]:
        if colors[i] == 0:
            dfs(i, 3-c)


t = int(input())
for i in range(t):
    V, E = map(int, input().split())
    a = [[] for i in range(V+1)]
    colors = [0 for i in range(V+1)]

    for j in range(E):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)

    for j in range(1, V+1):
        if colors[j] == 0:
            dfs(j, 1)

    chkBinary = True
    for j in range(1, V+1):
        for k in a[j]:
            if colors[j] == colors[k]:
                chkBinary = False

    if chkBinary:
        print('YES')
    else:
        print('NO')
