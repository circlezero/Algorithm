n = int(input())

a = list()
for i in range(n):
    s = input().split()

    size = len(a)
    if s[0] == 'push':
        a.append(s[1])
    elif s[0] == 'top':
        if size == 0: print(-1)
        else : print(a[size-1])
    elif s[0] == 'size':
        print(size)
    elif s[0] == 'empty':
        if size == 0: print(1)
        else: print(0)
    elif s[0] == 'pop':
        if size == 0: print(-1)
        else : print(a.pop())