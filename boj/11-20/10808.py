import sys
s = sys.stdin.readline().strip()
alpha = [0] * 26
for i in s:
    index = ord(i) - ord('a')
    alpha[index] += 1
print(' '.join(map(str, alpha)))
