import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())


def get_arg(n, a):
    num = 0
    i = a
    while i <= n:
        num += (n // i)
        i *= a
    return num


n2 = get_arg(n, 2) - get_arg(n-m, 2) - get_arg(m, 2)
n5 = get_arg(n, 5) - get_arg(n-m, 5) - get_arg(m, 5)
print(min(n2, n5))
