import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    tmp = a % 10
    if tmp == 0:
        tmp = 10
    arr = []
    while tmp not in arr:
        arr.append(tmp)
        if tmp == 10:
            break
        tmp = (tmp * a) % 10

    nb = b % len(arr)
    print(arr[nb-1])
