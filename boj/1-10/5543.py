import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
coke = int(input())
cider = int(input())

min_set = min(a, b, c) + min(coke, cider) - 50
print(min_set)
