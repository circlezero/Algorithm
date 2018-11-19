t = int(input())

for i in range(t):
    h, w, n = list(map(int, input().split()))
    s = input().split()
    

    a = 0
    b = 0
    if n % h == 0:
        a = n // h
        b = h
    else: 
        a = n // h + 1
        b = n % h
    if a < 10: a = '0' + str(a)
    res = f'{b}{a}'
    print(res)
