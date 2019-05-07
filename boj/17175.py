import sys
n = int(sys.stdin.readline())
f = [1] * 51
for i in range(2, 51):
    f[i] = (f[i-2] + f[i-1] + 1) % 1000000007

print(f[n])