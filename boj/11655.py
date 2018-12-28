import sys

s = sys.stdin.readline()
for i in s:
    if i == ' ':
        print(' ', end='')
    elif ord(i) >= ord('a') and ord(i) <= ord('z'):
        n = ord(i) - ord('a')
        m = (n + 13) % 26
        print(chr(m+ord('a')), end='')
        
    elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
        n = ord(i) - ord('A')
        m = (n + 13) % 26
        print(chr(m+ord('A')), end='')
    else:
        print(i, end='')