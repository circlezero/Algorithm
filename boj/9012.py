import sys
n = int(sys.stdin.readline())

def chkBracket(s):
    stackCnt = 0
    
    for i in s:
        if i == '(':
            stackCnt += 1
        elif i == ')':
            stackCnt -= 1
        if stackCnt < 0:
            break
    
    if stackCnt != 0:
        print('NO')
    else:
        print('YES')

for i in range(n):
    chkBracket(sys.stdin.readline())