import sys

s = sys.stdin.readline()
bar = 0
cnt = 0
for i in range(1, len(s)):
    if s[i-1] == '(':
        if s[i] == ')':
            cnt += bar
        elif s[i] == '(':
            bar += 1
    else:
        if s[i] == ')':
            bar -= 1
            cnt += 1
print(cnt)