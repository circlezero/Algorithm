import sys
input = sys.stdin.readline
A, B = map(int, input().split())
m = int(input())

res = 0
arr_base_A = map(int, input().split())

for (ind, val) in enumerate(arr_base_A):
    res += (val * pow(A, m-ind-1))

arr_base_B = []

while res > 0:
    arr_base_B.append(res % B)
    res = res // B

for i in arr_base_B[::-1]:
    print(i, end=' ')
