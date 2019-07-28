import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A, B = [], []
ans = []
for i in range(N):
    A.append(list(map(int, input().split())))

_, K = map(int, input().split())
for i in range(M):
    B.append(list(map(int, input().split())))

for i in range(N):
    row = []
    for k in range(K):
        col = 0
        for j in range(M):
            col += A[i][j] * B[j][k]
        print(col, end=' ')
        row.append(col)
    print()
    ans.append(row)

# for i in ans:
#     print(i)