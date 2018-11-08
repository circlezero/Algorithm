n = int(input())

for i in range(0, n):
    a = list(map(int, input().split()))
    sum = 0
    for j in range(1, len(a)):
        sum += a[j]

    avg = sum / a[0]
    cnt = 0
    for j in range(1, len(a)):
        if avg < a[j]: cnt += 1
    
    print('{0:.3f}%'.format((cnt / a[0]) * 100))
