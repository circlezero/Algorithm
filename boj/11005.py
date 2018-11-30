s = list(map(int, input().split()))
n = s[0]
b = s[1]
r = n % b
res = ''

def convert(r):
    if r >= 10: return chr(55+r)
    else: return str(r)

while n >= b:
    r = n % b
    n = n // b
    res += convert(r)
res += convert(n)

print(res[::-1])