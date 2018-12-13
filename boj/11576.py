s = list(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))[::-1]

def convert(num, base):
    if num is 0:
        return
    convert(num // base, base)
    print(num % base, end=" ")

num = 0
for i in range(m):
    num += (a[i] * (s[0] ** i))

convert(num, s[1])