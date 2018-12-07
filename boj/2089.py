s = int(input())

a = s // -2
b = s % -2
if s is 0:
    c = '0'
else:
    c = ''
while abs(s) > 0:
    if s is -1:
        c += '11'
        break
    elif s is 1:
        c += '1'
        break

    a = s // -2
    b = s % -2
    s = a

    if b is 0:
        c += '0'
    else:
        s += 1
        c += '1'

print(c[::-1])