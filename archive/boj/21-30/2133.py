import sys
n = int(sys.stdin.readline())
d = [0] * 31
d[0] = 1

for i in range(2, 31, 2):
    d[i] = 3 * d[i-2]

    for j in range(4, i+1, 2):
        d[i] = d[i] + (2 * d[i-j])
print(d[n])
