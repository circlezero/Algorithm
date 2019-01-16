import sys
t = int(sys.stdin.readline())
d = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for i in range(5, 101):
    d[i] = d[i-1] + d[i-5] 

for i in range(t):
    n = int(sys.stdin.readline())
    print(d[n])