n, b = map(int, input().split())

cArr = [str(i) for i in range(10)]
for i in range(26):
    alpha = ord('A') + i
    cArr.append(chr(alpha))

res = ''
while n >= b:
    r = n % b
    n = n // b
    res += cArr[r]
res += cArr[n]

print(res[::-1])