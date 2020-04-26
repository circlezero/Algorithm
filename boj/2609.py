import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

A, B = map(int, input().split())
g = gcd(A, B)
print(g)
print(A * B // g)