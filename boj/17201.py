import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline()

ans = 'Yes'
prev = 0
for i in s:
    if i == prev:
        ans = 'No'
        break
    prev = i

print(ans)