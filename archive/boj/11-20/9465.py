import sys
input = sys.stdin.readline
t = int(input())


def print_max_value(n, Stickers):
    d = [[0 for i in range(3)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, 3):
            d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
            d[i][1] = max(d[i-1][0], d[i-1][2]) + Stickers[1][i-1]
            d[i][2] = max(d[i-1][0], d[i-1][1]) + Stickers[2][i-1]

    print(max(d[n]))


for i in range(t):
    n = int(input())
    A = [[]]
    A.append(list(map(int, input().split())))
    A.append(list(map(int, input().split())))
    print_max_value(n, A)
