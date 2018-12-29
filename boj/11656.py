import sys

s = sys.stdin.readline().strip()[::-1]
a = []
t = ''
for i in s:
    t = i + t
    a.append(t)
a.sort()
print('\n'.join(a))
