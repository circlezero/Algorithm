import sys
input = sys.stdin.readline
A, B, V = map(int, sys.stdin.readline().split())
ans = (V-B) // (A-B)
if (V-A) % (A-B) != 0:
    ans += 1
print(ans)