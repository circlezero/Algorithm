n = int(input())

for i in range(n):
    s = input().split()
    ns = ''
    for i in s[1]:
        ns += i * int(s[0])
    print(ns)