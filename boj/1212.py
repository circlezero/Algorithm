import sys
input = sys.stdin.readline
o = f'0o{input()}'
b = f'{int(o, 8):b}'
print(b)
