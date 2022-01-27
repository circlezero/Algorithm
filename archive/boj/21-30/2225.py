import sys
n, k = map(int, sys.stdin.readline().split())
d = [[0 for i in range(201)] for i in range(201)]
mod = 1000000000
d[0][0] = 1
# d[k][n] : k개의 정수를 합쳐서 n이 되는 경우의 수

# 정수의 수를 하나씩 늘려가며
for i in range(1, k+1):

    # 합을 n이 되기 까지 작은 문제를 해결해나간다.
    for j in range(n+1):

        # 이전의 경우의 수를 합친다.
        for h in range(j+1):
            d[i][j] += d[i-1][j-h]
            d[i][j] %= mod
print(d[k][n])
