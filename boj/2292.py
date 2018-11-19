n = int(input())

if n == 1: print(1)
else: 
    t = n - 1
    cnt = 1
    while True:
        if t <= (6 * cnt): 
            cnt += 1
            break
        t = t - (6 * cnt)
        cnt += 1
    print(cnt)