
n = int(input())
d = [0] * 100001

for i in range(n+1):
    d[i] = i
    j = 1
    while j * j <= i:
        ind = i - (j * j)
        if d[i] > d[ind] + 1:
            d[i] = d[ind] + 1
        j += 1

print(d[n])
