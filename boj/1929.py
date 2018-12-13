m, n = list(map(int, input().split()))
a = [1] * 1000001
a[0] = 0
a[1] = 0

i = 2
while i*i <= 1000000:
    if a[i] is 0:
        i += 1
        continue
    else:
        j = 2
        while i*j <= 1000000:
            a[i * j] = 0
            j += 1
        i += 1
        
for i in range(m, n+1):
    if a[i] is 1:
        print(i)