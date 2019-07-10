import sys
a = list(map(int, sys.stdin.readline().split()))
a.sort()
ans = 1
for i in range(len(a)):
    if i+1 != a[i]:
        ans = 0
        break
print(ans) 