import sys
input = sys.stdin.readline
MAX = 123456 * 2

chk = [True] * (MAX + 1)
chk[0] = False
chk[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if chk[i]:
        j = 2
        while i * j < MAX + 1:
            chk[i*j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if chk[i]:
            cnt += 1

    print(cnt)
