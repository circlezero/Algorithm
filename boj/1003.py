import sys
t = int(sys.stdin.readline())
fibo = [0] * 41

def fibonachi(num):
    if num == 1:
        return 1
    else:
        res = 0
        if fibo[num-1] != 0:
            res += fibo[num-1]
        if fibo[num-1] != 0:
            res += fibo[num-2]
        return res

for i in range(1, 41):
    fibo[i] = fibonachi(i)

for i in range(t):
    n = int(sys.stdin.readline())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        print(f"{fibo[n-1]} {fibo[n]}")