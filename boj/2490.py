import sys

for i in range(3):
    s = list(map(int, sys.stdin.readline().split()))
    cnt = s.count(0)
    ans = 'E'
    if cnt == 1:
        ans = 'A'
    elif cnt == 2:
        ans = 'B'
    elif cnt == 3:
        ans = 'C'
    elif cnt == 4:
        ans = 'D'
    print(ans)