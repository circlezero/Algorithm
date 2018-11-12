a = int(input())
b = int(input())
c = int(input())

num = [0] * 10
res = str(a * b * c)
for i in range(len(res)):
    num[int(res[i])] += 1
for i in range(10):
    print(num[i])