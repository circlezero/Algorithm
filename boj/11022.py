import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    a.append((A, B))

for i in range(n):
    print(f'Case #{i+1}: {a[i][0]} + {a[i][1]} = {a[i][0] + a[i][1]}')