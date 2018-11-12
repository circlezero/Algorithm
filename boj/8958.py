n = int(input())

for i in range(n):
    s = input()
    acc = 0
    sum = 0
    for j in range(len(s)):
        if s[j] == 'X': acc = 0
        elif s[j] == 'O':
            acc += 1
            sum += acc
    print(sum)