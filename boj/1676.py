import math
num = int(input())
five_cnt = 0
two_cnt = 0
n = math.factorial(num)

while n % 5 == 0:
    five_cnt += 1
    n = n // 5

while n % 2 == 0:
    two_cnt += 1
    n = n // 2

print(min([five_cnt, two_cnt]))