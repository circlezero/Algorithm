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
    num, *arr = map(int, input().split())
    comb = combinations(arr, 2)
    gSum = 0
    for j in comb:
        gSum += gcd(*j)
    print(gSum)
        