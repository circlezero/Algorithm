n, r = list(map(int, input().split()))

def get_arg(n, a):
    num = 0
    i = a
    while i <= n:
        num += (n // i)
        i *= a
    return num

cnt_two = get_arg(n, 2) - get_arg(r, 2) - get_arg(n-r, 2)
cnt_five = get_arg(n, 5) - get_arg(r, 5) - get_arg(n-r, 5)

print(min(cnt_five, cnt_two))