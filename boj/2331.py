import sys

a, p = map(int, sys.stdin.readline().split())
arr = []
arr.append(a)
currentNum = a
res = 0

def getNextNum(number):
    res = 0
    while number > 0:
        res += (number % 10) ** p
        number = number // 10
    return res

while True:
    nextNum = getNextNum(currentNum)
    try:
        index = arr.index(nextNum)
        if index >= 0:
            res = index
            break
    except ValueError:
        arr.append(nextNum)
        currentNum = nextNum

print(res)