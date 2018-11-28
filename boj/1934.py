t = int(input())

def gcd(a, b):
    r = a % b
    if r == 0: return b
    while r > 0:
        r = a % b
        a = b
        b = r
    return a

for i in range(t):
    a, b = list(map(int, input().split()))
    print(int(a*b / gcd(b,a)))