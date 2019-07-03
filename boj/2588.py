import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().strip()
for i in b[::-1]:
    print(a * int(i))
print(a * int(b))