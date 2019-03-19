import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[-1 for i in range(n+1)] for j in range(n+1)]
dist = [0 for i in range(n+1)]
res = 1

for i in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(s) - 1, 2):
        dist[s[0]][s[j]] = s[j+1]