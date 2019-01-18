import sys
s = sys.stdin.readline()
sl = len(s)
mod = 1000000
d = [0] * 5001

d[0] = 1
for i in range(sl):
    j = i + 1
    n = int(s[i])
    m = int(s[i-1] + s[i])
    if n > 0 and n < 10:
        d[j] += d[j-1]
        d[j] %= mod
    if m >= 10 and m <= 26:
        d[j] += d[j-2]
        d[j] %= mod
print(d[sl])