s = input()
a = [0] * 10

for i in s:
    a[int(i)] += 1

max = 0
for i in range(10):
    if i == 6 or i == 9:
        continue
    if a[i] > max:
        max = a[i]

if max < (a[6] + a[9] + 1) // 2:
    max = (a[6] + a[9] + 1) // 2
print(max)