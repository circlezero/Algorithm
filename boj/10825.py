import sys
n = int(sys.stdin.readline())
a = []

def sortName(el):
    return el[0]

def sortKor(el):
    return el[1]

def sortEng(el):
    return el[2]

def sortMath(el):
    return el[3]

for i in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    a.append((name, int(kor), int(eng), int(math)))

a.sort(key=sortName)
a.sort(key=sortMath, reverse=True)
a.sort(key=sortEng)
a.sort(key=sortKor, reverse=True)

for i in a:
    print(i[0])
