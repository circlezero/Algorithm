import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

na = {}
for i in a:
    if i in na:
        na[i] += 1
    else:
        na[i] = 1

for i in b:
    if i in na:
        print(na[i], end=' ')
    else:
        print('0', end=' ')
