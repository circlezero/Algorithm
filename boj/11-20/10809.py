import sys
s = sys.stdin.readline().strip()
alpha = [-1] * 26

for ind, ch in enumerate(s):
    index = ord(ch) - ord('a')
    if alpha[index] == -1:
        alpha[index] = ind

print(' '.join(map(str, alpha)))
