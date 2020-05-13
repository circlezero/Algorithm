import sys
from itertools import combinations
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

t = int(input())
for i in range(t):
    n, *arr = map(int, input().split())
    leng = len(arr)

    res = 0
    for (a, b) in list(combinations(arr, 2)):
        res = res + gcd(a, b)
    print(res)
    # for one in range(leng):
    #     for two in range(one+1, leng):
    #         res = res + gcd(arr[one], arr[two])
    # print(res)