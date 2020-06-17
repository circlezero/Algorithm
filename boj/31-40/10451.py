import sys
input = sys.stdin.readline


def dfs(x, v, a):
    v[x] = True
    next = a[x]
    if v[next] is False:
        dfs(next, v, a)


t = int(input())
for i in range(t):
    n = int(input())
    v = [False for j in range(n+1)]
    a = [0] + list(map(int, input().split()))

    cnt = 0
    for j in range(1, n+1):
        if v[j] is False:
            cnt += 1
            dfs(j, v, a)
    print(cnt)
