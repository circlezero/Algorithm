s = input()
a = [-1]*26

for i in range(len(s)):
    ind = ord(s[i]) - ord('a')
    if a[ind] == -1:
        a[ind] = i

for i in a:
    print(i, end=" ")