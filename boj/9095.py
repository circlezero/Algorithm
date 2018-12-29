t = int(input())
for i in range(t):
    n = int(input())
    d = [1] * 11
    d[2] = 2
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])