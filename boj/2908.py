s = input().split()

a = ''
b = ''
for i in range(2, -1, -1):
    a += s[0][i]
    b += s[1][i]

if int(a) > int(b): print(a)
else: print(b)