import sys

n = int(sys.stdin.readline())
a = []
b = []
c = []

def gcd(a, b):
    r = a % b
    while r > 0:
        r = a % b
        a = b
        b = r
    return a

for i in range(n):
    a.append(int(sys.stdin.readline()))

for i in range(n-1):
    b.append(abs(a[i]-a[i+1]))

minGcd = 1000000000
for i in range(len(b)-1):
    minGcd = min(minGcd, gcd(b[i], b[i+1]))

aSize = a[len(a)-1] - a[0]
ans = (aSize // minGcd) + 1 - len(a)
print(ans)