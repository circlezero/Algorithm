import sys
n = 1000 - int(sys.stdin.readline())
ans = 0

if n >= 500:
    ans += (n // 500)
    n = n % 500

if n >= 100:
    ans += (n // 100)
    n = n % 100

if n >= 50:
    ans += (n // 50)
    n = n % 50

if n >= 10:
    ans += (n // 10)
    n = n % 10

if n >= 5:
    ans += (n // 5)
    n = n % 5

ans += n
print(ans)