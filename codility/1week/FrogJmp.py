import sys
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
d = int(sys.stdin.readline())
ans = 0
dist = y - x
if dist % d == 0:
    ans = dist // d
else:
    ans = dist // d + 1
print(ans)