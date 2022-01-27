t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
n = len(t)
t.append([0 for i in range(n+1)])

a = [[0 for i in range(n+1)] for j in range(n+1)]
a[0][0] = t[0][0]
for i in range(n):
    for j in range(i+1):
        a[i+1][j] = max(a[i+1][j], a[i][j] + t[i+1][j])
        a[i+1][j+1] = max(a[i+1][j+1], a[i][j] + t[i+1][j+1])

print(max(a[n-1]))