import sys
input = sys.stdin.readline
n = int(input())
arr = map(int, input().split())

prime_map = [1] * 1001
prime_map[0] = 0
prime_map[1] = 0
i = 2

while(i*i < 1001):
    if prime_map[i] == 0:
        i += 1
    else:
        for j in range(2, 1001):
            if i * j > 1000:
                break
            else:
                prime_map[i*j] = 0
        i += 1

cnt = 0
for i in arr:
    if prime_map[i] == 1:
        cnt += 1
print(cnt)
