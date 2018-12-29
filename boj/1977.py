n = int(input())
m = int(input())
pow_list = []
res = 0
i = 1
while i*i <= m:
    if i*i >= n:
        res += (i*i)
        pow_list.append(i*i)
    i += 1

if len(pow_list) == 0:
    print('-1')
else:
    print(res)
    print(pow_list[0])