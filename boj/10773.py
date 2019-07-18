import sys
input = sys.stdin.readline

k = int(input())
a = list()
for i in range(k):
    num = int(input())
    if num == 0:
        a.pop()
    else:
        a.append(num)
print(sum(a))
