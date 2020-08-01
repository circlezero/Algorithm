import sys
s = sys.stdin.readline()
for i in s:
    ind = ord(i)
    if ord('a') <= ord(i) <= ord('z'):
        ind = ord('a') + (ord(i) - ord('a') + 13) % 26

    elif ord('A') <= ord(i) <= ord('Z'):
        ind = ord('A') + (ord(i) - ord('A') + 13) % 26
    print(chr(ind), end='')
