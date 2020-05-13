import sys
input = sys.stdin.readline
M, N = map(int, input().split())

MAX_NUM = 1_000_001
A = [1] * MAX_NUM
A[0] = 0
A[1] = 0
i = 2

while i * i < MAX_NUM:
    if A[i] == 0:
        i += 1
        continue
    else:
        for j in range(2, MAX_NUM):
            if i * j > MAX_NUM-1:
                break
            else:
                A[i*j] = 0
        i += 1

for i in range(M, N+1):
    if A[i] == 1:
        print(i)
