import sys
from operator import itemgetter
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    name, kor, eng, math = input().split()
    arr.append((int(kor), int(eng), int(math), name))

arr.sort(key=lambda elem: elem[3])
arr.sort(key=lambda elem: elem[2], reverse=True)
arr.sort(key=lambda elem: elem[1])
arr.sort(key=lambda elem: elem[0], reverse=True)

for i in arr:
    print(i[3])
