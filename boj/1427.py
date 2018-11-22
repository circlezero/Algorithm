s = input()
a = list()
for i in s:
    a.append(int(i))

a.sort(reverse=True)

for i in a:
    print(i, end='')