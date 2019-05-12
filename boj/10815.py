import sys

n = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))
an.sort()

m = int(sys.stdin.readline())
am = list(map(int, sys.stdin.readline().split()))

def binarySearch(start, end, target):
    if start == end:
        if an[start] == target:
            return 1
        else:
            return 0
    mid = (end+start) // 2
    if an[mid] == target:
        return 1
    elif an[mid] > target:
        return binarySearch(start, mid, target)
    elif an[mid] < target:
        return binarySearch(mid+1, end, target)

def check(num):
    return binarySearch(0, n-1, num)

for i in am:
    print(check(i), end=" ")