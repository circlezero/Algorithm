s = input()
n = 0
for i in s:
    n += 1
    print(i, end="")
    if (n) % 10 == 0:
        print('')