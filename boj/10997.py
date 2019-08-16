import sys
n = int(sys.stdin.readline())
star = ['*****', '*', '* ***', '* * *', '* * *', '*   *', '*****']
if n == 1:
    print('*')
else:
    W = 5
    H = 7
    for i in range(2, n):
        for i in range(H):
            if i == 0:
                star[i] = f'* {star[i]}**'
            elif i == 1:
                star[i] = '* ' + star[i] + ' '*W + '*'
            else:
                star[i] = f'* {star[i]} *'
        
        base = '*'*(W+4)
        star = [base, '*'] + star + ['*' + ' '*(W+2) + '*' , base]

        W += 4
        H += 4

    for i in star:
        print(i)
    