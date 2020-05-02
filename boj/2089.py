import sys
input = sys.stdin.readline
n = int(input())

a = n // -2
b = n % -2
c = ''
if n == 0:
    c = '0'

while abs(n) > 0:
    if n == -1:
        c += '11'
        break
    elif n == 1:
        c += '1'
        break

    a = n // -2
    b = n % -2
    n = a

    if b == 0:
        c += '0'
    else:
        n += 1
        c += '1'
print(c[::-1])
