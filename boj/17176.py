import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
s = list(sys.stdin.readline().strip())
arr = []
for i in s:
    if i == ' ':
        arr.append(0)
    elif ord('A') <= ord(i) <= ord('Z'):
        arr.append(ord(i)-ord('A')+1)
    elif ord('a') <= ord(i) <= ord('z'):
        arr.append(ord(i)-ord('a')+27)
arr.sort()

ans = 'y'
for i in range(n):
    if a[i] != arr[i]:
        ans = 'n'
        break
print(ans)