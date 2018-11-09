import math
s = ['  *   ', ' * *  ', '***** ']

def make_star(n):
    l = len(s)
    for i in range(l):
        s.append(s[i] + s[i])
        s[i] = ('   ' * n) + s[i] + ('   ' * n)

n = int(input())
k = int(math.log(int(n / 3), 2))

for i in range(k):
    make_star(pow(2,i))

print('\n'.join(s))
# for i in range(n):
#     print(s[i])