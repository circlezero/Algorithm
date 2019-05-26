import sys
start = int(sys.stdin.readline())
end = int(sys.stdin.readline())
isPrime = [False, False] + [True] * 10000

for i in range(2, int(10000 ** 0.5) + 1):
    if isPrime[i]:
        ind = 2
        while ind * i <= 10000:
            isPrime[ind * i] = False
            ind += 1

ans = 0
minValue = 0
for i in range(start, end+1):
    if isPrime[i]:
        if minValue == 0:
            minValue = i
        ans += i

if ans == 0:
    print(-1)
else:
    print(ans, minValue)