s = input().split()
n = s[0][::-1]
b = int(s[1])

sum = 0
for i in range(len(n)):
    if ord(n[i]) >= 65:
        sum += ( ord(n[i]) - 55) * (b ** i)
    else:
        sum += int(n[i]) * (b ** i)
print(sum)