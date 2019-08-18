import sys
n = int(sys.stdin.readline())

def makeTriangle(W, H, A):
    prev = len(A)
    ans = []
    ans.append(' '*(H-1) + '*')
    RT = A[::-1]
    for i in range(1, H-1):
        if i < prev:
            ans.append(' '*(H-1-i)+'*'+' '*(2*i-1)+'*')
        else:
            ans.append(' '*(H-1-i)+'*'+ ' '*(i-prev) + RT[i-prev] + ' '*((i-prev)*2) + '*')
    ans.append('*'*W)
    return ans

ans = ['*']
H = 1
W = 1

for i in range(1, n):
    H = 2*H + 1
    W = 2*W + 3
    ans = makeTriangle(W,H,ans)

if n % 2 == 0:
    ans = ans[::-1]

for i in ans:
    print(i)