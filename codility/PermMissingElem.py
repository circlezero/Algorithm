import sys
a = list(map(int, sys.stdin.readline().split()))
arr = []
for i in a:
    arr.append(i)
arr.sort()

prev = 1
if len(arr) != 0:
    prev = arr[0]
ans = 1

for i in arr:
    if i == prev:
        continue
    
    if prev + 1 != i:
        ans = prev + 1
        break
    prev = i
print(prev)