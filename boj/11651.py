import sys
input = sys.stdin.readline
n = int(input())
arr = list()
for i in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))

arr.sort()

for y, x in arr:
    print(x, y)
