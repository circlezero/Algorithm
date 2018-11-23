t = int(input())
a = list()
for i in range(t):
    s = input()
    a.append(s)

a = list(set(a))
a.sort()
a.sort(key=len)

for i in a:
    print(i)