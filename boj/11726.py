n = int(input())
d = [1] * 1001
d[2] = 2

for i in range(2, n+1):
    d[i] = (d[i-1] + d[i-2]) % 10007
print(d[n])