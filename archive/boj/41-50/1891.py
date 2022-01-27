import sys
input = sys.stdin.readline
d, n = map(int, input().split())
x, y = map(int, input().split())


def get_location(d, num):
    if d == 1:
        if num == '1':
            return (1, 0)
        elif num == '2':
            return (0, 0)
        elif num == '3':
            return (0, 1)
        elif num == '4':
            return (1, 1)

    else:
        next_num = num[1:]
        nx, ny = get_location(d-1, next_num)
        p_num = 2 ** (d-1)
        if num[0] == '1':
            return (nx + p_num, ny)
        elif num[0] == '2':
            return (nx, ny)
        elif num[0] == '3':
            return (nx, ny + p_num)
        elif num[0] == '4':
            return (nx + p_num, ny + p_num)


def get_num(d, x, y):
    if d == 0:
        return ''

    unit = 2 ** (d-1)
    # 1 사분면
    if x >= unit and y < unit:
        return '1' + get_num(d-1, x-unit, y)
    # 2 사분면
    elif x < unit and y < unit:
        return '2' + get_num(d-1, x, y)
    # 3 사분면
    elif x < unit and y >= unit:
        return '3' + get_num(d-1, x, y-unit)
    # 4 사분면
    elif x >= unit and y >= unit:
        return '4' + get_num(d-1, x-unit, y-unit)


nx, ny = get_location(d, str(n))
if (nx + x < 0) or (nx + x >= 2 ** d) or (ny - y >= 2 ** d) or (ny - y < 0):
    res = -1
else:
    res = get_num(d, nx + x, ny - y)
print(res)
