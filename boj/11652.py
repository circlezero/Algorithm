import sys
input = sys.stdin.readline
n = int(input())
obj = {}
for i in range(n):
    num = int(input())
    if num in obj:
        obj[num] += 1
    else:
        obj[num] = 1

sorted_obj = dict(sorted(obj.items()))
print(max(sorted_obj, key=sorted_obj.get))
