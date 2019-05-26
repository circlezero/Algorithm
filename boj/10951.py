import sys

lines = sys.stdin.readlines()
for i in lines:
    a, b = map(int, i.strip().split())
    print(a + b)