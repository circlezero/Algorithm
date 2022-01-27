import sys
input = sys.stdin.readline
n = int(input())
res = []


def hanoi(s, e, c):
    if c == 0:
        return
    hanoi(s, 6-s-e, c-1)
    print(s, e)
    hanoi(6-s-e, e, c-1)


print(2**n - 1)
hanoi(1, 3, n)
