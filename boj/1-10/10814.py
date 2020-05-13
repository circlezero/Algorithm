import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append((int(age), name))
arr.sort(key=lambda elem: elem[0])
for age, name in arr:
    print(age, name)
