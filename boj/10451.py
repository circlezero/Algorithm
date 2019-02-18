import sys
sys.setrecursionlimit(2000)
check = [False] * (1001)
def dfs(start):
    if check[start] == True:
        return
    check[start] = True
    dfs(arr[start-1])

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    check = [False] * (n+1)
    res = 0
    for j in range(1, n+1):
        if check[j] == False:
            dfs(j)
            res += 1
    
    print(res)