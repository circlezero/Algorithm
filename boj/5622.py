a = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
n = [0]*10
for i in range(1,10):
    n[i] = i + 1

s = input()
sum = 0
for i in s:
    ind = ord(i) - ord('A')
    sum += n[a[ind]]

print(sum)