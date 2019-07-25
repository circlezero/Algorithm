import sys
n = int(sys.stdin.readline())

def makeStar(n):
    if n == 3:
        return ['***', '* *', '***']
    k = n // 3
    blank = ' ' * k
    star = makeStar(k)
    ans = []
    for i in range(n):
        if i >= k and i < k+k:
            ans.append(star[i % k] + blank + star[i % k])
        else:
            ans.append(star[i % k] * 3)
    return ans
for i in makeStar(n):
    print(i)