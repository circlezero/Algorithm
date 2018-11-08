import sys

n = int(sys.stdin.readline())
for i in range(0, n):
    res = eval(sys.stdin.readline().replace(' ', '+'))
    print(res)