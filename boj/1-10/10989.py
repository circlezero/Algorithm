import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
for i in range(n):
    t = int(input())
    arr[t] += 1

for i in range(1, 10001):
    if arr[i] > 0:
        for j in range(arr[i]):
            print(i)
