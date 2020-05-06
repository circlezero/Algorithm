import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    name, kor, eng, math = input().split()
    arr.append((kor, eng, math, name))
