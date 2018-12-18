import sys
n = int(sys.stdin.readline())
a = []
def getSecond(e):
    return e[1]
for i in range(n):
    age, name = sys.stdin.readline().split()
    a.append((name, int(age)))
a.sort(key=getSecond)
for i in a:
    print(f'{i[1]} {i[0]}')