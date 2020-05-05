import sys
import math
input = sys.stdin.readline
n = int(input())
n2 = 0
n5 = 0
for i in range(2, n+1):
    t = i
    if t % 5 == 0:
        while t % 5 == 0:
            n5 += 1
            t = t // 5
    if t % 2 == 0:
        while t % 2 == 0:
            n2 += 1
            t = t // 2
print(min(n2, n5))
