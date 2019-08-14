import sys
n = int(sys.stdin.readline())
s = ['* ', ' *']
ans = ['','']

for i in range(n):
    ans[i%2] += s[i%2]

if n == 1:
    print(s[0])
else:
    for i in range(2*n):
        print(ans[i%2])
    