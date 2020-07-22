import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())


def get_num(n, r, c):

    if n == 1:
        return 2*r + c

    else:
        unit = 2 ** (n-1)
        size = unit ** 2
        if r < unit and c < unit:
            # 0 에 해당하는 부분
            return get_num(n-1, r, c)
        elif r < unit and c >= unit:
            # 1에 해당하는 부분
            return get_num(n-1, r, c - unit) + size
        elif r >= unit and c < unit:
            # 2에 해당하는 부분
            return get_num(n-1, r - unit, c) + size * 2
        elif r >= unit and c >= unit:
            # 3에 해당하는 부분
            return get_num(n-1, r-unit, c-unit) + size * 3


res = get_num(n, r, c)
print(res)
