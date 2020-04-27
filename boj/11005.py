import sys
input = sys.stdin.readline
n, b = map(int, input().split())


def conversion(num):
    if num < 10:
        print(num, end='')
    else:
        print(chr(ord('A') - 10 + num), end='')


arr = []

while n >= b:
    r = n % b
    n = n // b
    arr.append(r)
arr.append(n)

for i in arr[::-1]:
    conversion(i)
