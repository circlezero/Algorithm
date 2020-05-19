import sys
s = sys.stdin.readline().strip()
arr = []
leng = len(s)
for i in range(leng):
    arr.append(s[i:])

arr.sort()
for i in arr:
    print(i)
