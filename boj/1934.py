import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    l = a * b // g
    print(l)
