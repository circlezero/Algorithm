import sys
sys.setrecursionlimit(200002)

t = int(sys.stdin.readline())
color = [0] * 20002
arr = [[] for i in range(20002)]

def dfs(start, c):
    color[start] = c
    for i in arr[start]:
        if color[i] == 0:
            dfs(i, 3-c)

for i in range(t):
    v, e = list(map(int, sys.stdin.readline().split()))
    arr = [[] for j in range(v + 1)]
    color = [0] * (v + 1)

    for j in range(e):
        U, V = list(map(int, sys.stdin.readline().split()))
        arr[U].append(V)
        arr[V].append(U)
    
    for j in range(1, v+1):
        if color[j] == 0:
            dfs(j, 1)

    chkBinary = True    
    for j in range(1, v+1):
        for k in arr[j]:
            if color[j] == color[k]:
                chkBinary = False

    if chkBinary:
        print("YES")
    else:
        print("NO")