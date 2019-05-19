import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def sum(num):
    ans = 0
    ans = (num * (num+1)) // 2
    return ans

def ans(num):
    result = 0
    result += 3 * sum(num // 3)
    result += 7 * sum(num // 7)
    result -= 21 * sum(num // 21)
    print(result)

for i in a:
    ans(i)