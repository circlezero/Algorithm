import sys
input = sys.stdin.readline
n = int(input())


def stack(arr, cmd, num):
    if cmd == 'push':
        arr.append(num)
    elif cmd == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif cmd == 'size':
        print(len(arr))
    elif cmd == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            last = len(arr)-1
            print(arr[last])


arr = []
for i in range(n):
    op = input().split()
    num = -1
    if len(op) > 1:
        num = op[1]
    stack(arr, op[0], num)
