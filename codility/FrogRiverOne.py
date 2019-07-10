import sys
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

ans = [False for i in range(x)]

cnt = 0
for i in range(len(a)):
    if ans[a[i]-1] == False:
        ans[a[i]-1] = True
        cnt += 1
    if cnt == x:
        print(i)
        break
        