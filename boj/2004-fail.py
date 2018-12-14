import math
n, r = list(map(int, input().split()))
c = math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
c = str(c)[::-1]
for i in range(len(c)):
    if c[i] is not '0':
        print(i)
        break