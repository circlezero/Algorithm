a = list(map(int, input().split()))

if a[0] < a[1]: f = 1
elif a[0] > a[1]: f = 2

for i in range(1, len(a)-1):
    if f == 1 and a[i] > a[i+1]:
        f = 3
        break
    if f == 2 and a[i] < a[i+1]:
        f = 3
        break
        
if f == 1: print('ascending')
elif f == 2: print('descending')
else: print('mixed')