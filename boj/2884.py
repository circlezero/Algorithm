import sys
h, m = map(int, sys.stdin.readline().split())
M = m - 45
H = h
if M < 0:
    H = h-1
    M = 60 + M
if H < 0:
    H = 23
print(H,M)