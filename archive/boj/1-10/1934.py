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
    A, B = map(int, input().split())
    g = gcd(A, B)
    l = A * B // g
    print(l)