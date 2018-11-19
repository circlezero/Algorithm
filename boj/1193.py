n = int(input())
a = 1
b = 1
t = n
cnt = 1
while True:
    if t <= cnt: break
    t -= cnt
    cnt += 1

if cnt % 2 == 0:
    a = t
    b = cnt -t + 1
else:
    b = t
    a = cnt -t + 1

print(f'{a}/{b}')