import sys


def calc_num(s):
    a = 0
    A = 0
    num = 0
    sp = 0
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            a += 1
        elif ord('A') <= ord(i) <= ord('Z'):
            A += 1
        elif ord('0') <= ord(i) <= ord('9'):
            num += 1
        elif i == ' ':
            sp += 1
    print(f'{a} {A} {num} {sp}')


while True:
    s = sys.stdin.readline().strip('\n')
    if s == '':
        break
    calc_num(s)
