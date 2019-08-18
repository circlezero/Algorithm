import sys
n = int(sys.stdin.readline())

s = '*' * n
bet = (n - 2)
blank = bet * 2 + 1
ans = []

ans.append(s + ' '*blank + s)
for i in range(1, n-1):
    si = '*' + ' '*bet + '*'
    ans.append(' '*i + si + ' '*(blank - 2*i) + si)
ans.append(' '*(n-1) + '*'+ ' '*bet + '*' + ' '*bet + '*')

for i in ans:
    print(i)

for i in ans[n-2::-1]:
    print(i)