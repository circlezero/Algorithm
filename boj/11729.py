import sys
n = int(sys.stdin.readline())

ans = 0
def hanoi(N, from_col, to_col, aux_col):
    if N == 1:
        print(from_col, to_col)
        return 
    hanoi(N-1, from_col, aux_col, to_col)
    print(from_col, to_col)
    hanoi(N-1, aux_col, to_col, from_col)

print(2**n - 1)
hanoi(n, 1, 3, 2)