t = int(input())

def getMaxScore(a, d, n):
    for i in range(1, n+1):
        d[i][0] = max(d[i-1][0], d[i-1][1] + a[0][i-1], d[i-1][2] + a[1][i-1])
        d[i][1] = max(d[i-1][0], d[i-1][2] + a[1][i-1])
        d[i][2] = max(d[i-1][0], d[i-1][1] + a[0][i-1])
    return max(d[n][0], d[n][1], d[n][2])

for i in range(t):
    n = int(input())
    a = [[0 for i in range(n)] for j in range(2)]
    d = [[0 for i in range(3)] for j in range(n+1)]

    a[0] = list(map(int, input().split()))
    a[1] = list(map(int, input().split()))

    print(getMaxScore(a, d, n))