import sys

n, k = map(int, sys.stdin.readline().split())
coin = []

for i in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)

ans = 0
for i in coin:
    ans += (k // i)
    k = (k % i)

print(ans)