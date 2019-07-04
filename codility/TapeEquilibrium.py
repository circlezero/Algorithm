import sys
A = list(map(int, sys.stdin.readline().split()))
print(A)

a = 0
b = sum(A)
ans = 100000

for i in range(len(A)-1):
    a += A[i]
    b -= A[i]
    ans = min(ans, abs(a-b))
    print(ans, a, b, abs(a-b))
print(ans)