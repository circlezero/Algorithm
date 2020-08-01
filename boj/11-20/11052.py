import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

for i in range(1, n+1):
    comp_arr = []
    for j in range(i+1):
        comp_arr.append(d[i-j] + a[j])
    d[i] = max(comp_arr)

print(d[n])
