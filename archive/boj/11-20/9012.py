import sys
input = sys.stdin.readline
n = int(input())


def check_brakets(braket_str):
    sum = 0
    for i in braket_str:
        if sum < 0:
            break

        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1

    if sum == 0:
        print('YES')
    else:
        print('NO')


for i in range(n):
    check_brakets(input())
