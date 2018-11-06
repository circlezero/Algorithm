n = int(input())
ff = int(n / 5)
tf = int(n / 3)

while ff > 0:
    tmp = n - (ff * 5)
    if tmp % 3 == 0:
        tf = int(tmp / 3)
        break
    ff = ff - 1

if((ff * 5 + tf * 3) - n == 0): print(ff + tf)
else: print(-1)