a = int(input())
arr = [1]*100 + [0]*901

for i in range(100, 1001):
    n0 = int(i / 100)
    n1 = int(i / 10 % 10) 
    n2 = i % 10

    if (n0 - n1) == (n1 - n2):
        arr[i] = 1

cnt = 0
for i in range(1, a+1):
    if arr[i] == 1: cnt += 1

print(cnt)