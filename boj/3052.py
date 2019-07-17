import sys
a = list()
for i in range(10):
    a.append(int(sys.stdin.readline()) % 42)
print(len(set(a)))