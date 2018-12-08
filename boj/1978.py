n = int(input())
s = list(map(int, input().split()))

a = [1] * 1001
a[0] = 0; a[1] = 0; i = 2

while i*i <= 1001:
    if a[i] is 0:
        i += 1; continue
    else:
        for j in range(2, 1001):
            if j * i > 1000:
                break
            else:
                a[i*j] = 0
        i += 1
cnt = 0
for i in s:
    if a[i] is 1:
        cnt += 1
print(cnt)