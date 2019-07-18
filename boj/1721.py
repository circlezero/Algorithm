import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
ans = -1
profit = C - B
if profit > 0:
    ans = (A // profit) + 1
print(ans)