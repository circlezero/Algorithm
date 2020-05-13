import sys
input = sys.stdin.readline
n = int(input())
i = 2

while i * i <= n:
    while n % i == 0:
        n = n // i
        print(i)
    i += 1

if n > 1:
    print(n)
