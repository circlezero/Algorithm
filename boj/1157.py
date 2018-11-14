s = input().upper()
a = [0] * 26
an = ord('A')

for i in s:
    ind = ord(i) - an
    a[ind] += 1

max = 0; dup = 0; ind = 0

for i in range(len(a)):
    if max == a[i]:
        dup += 1

    if max < a[i]:
        ind = i
        max = a[i]
        dup = 0

if dup > 0: print('?')
else: print(chr(an + ind))