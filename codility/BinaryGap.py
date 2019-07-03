import sys
n = int(sys.stdin.readline())
s = bin(n)
ans = 0
tmp = 0
print(s[2:])
for i in s[2:]:
    if i == '1':
        if ans < tmp:
            ans = tmp
        tmp = 0
    else:
        tmp += 1
print(ans)