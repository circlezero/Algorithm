import math
n = int(input())
res = str(math.factorial(n))[::-1]
for i in range(len(res)):
    if res[i] != '0':
        print(i)
        break