import sys

def printFunc(s):
    under_cnt = 0
    upper_cnt = 0
    num_cnt = 0
    space_cnt = 0
    for i in s:
        if i == ' ':
            space_cnt += 1
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            upper_cnt += 1
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            under_cnt += 1
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            num_cnt += 1
    print(f'{under_cnt} {upper_cnt} {num_cnt} {space_cnt}')


s = sys.stdin.readlines()
for i in s:
    printFunc(i)