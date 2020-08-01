import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))
c = ["0"] * m


def bin_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return True
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


for i in range(m):
    if bin_search(b[i], 0, n-1):
        c[i] = "1"

print(' '.join(c))
