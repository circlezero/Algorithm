import sys

s = list(sys.stdin.readline().strip().split('-'))
num = []

def convertInt(s):
    l = list(map(int, s.split('+')))
    return sum(l)

for i in s:
    num.append(convertInt(i))

ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]

print(ans)