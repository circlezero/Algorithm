t = int(input())

def gcd(a, b):
    if a < b:
        t = a; a = b; b = t

    r = a % b
    if r == 0: return b
    while r > 0:
        r = a % b; a = b; b = r
    return a

for i in range(t):
    s = list(map(int, input().split()))
    sum = 0
    for i in range(1, s[0]+1):
        for j in range(i+1, s[0]+1):
            sum += gcd(s[i], s[j])
    print(sum)