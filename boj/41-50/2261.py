import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
a.sort()


def get_distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


def get_closest(x, y):
    n = y - x + 1
    if n == 1:
        return 0
    elif n == 2:
        return get_distance(a[x], a[x+1])
    elif n == 3:
        n1 = get_distance(a[x], a[x+1])
        n2 = get_distance(a[x], a[x+2])
        n3 = get_distance(a[x+1], a[x+2])
        return min(n1, n2, n3)

    mid = (x + y) // 2
    left = get_closest(x, mid)
    right = get_closest(mid+1, y)
    ans = min(left, right)

    b = list()
    for i in range(x, y+1):
        d = a[i][0] - a[mid][0]
        if d ** 2 < ans:
            b.append(a[i])

    b.sort(key=lambda a: a[1])
    m = len(b)
    for i in range(0, m-1):
        for j in range(i+1, m):
            y = b[j][1] - b[i][1]
            if y ** 2 < ans:
                d = get_distance(b[i], b[j])
                if d < ans:
                    ans = d
            else:
                break

    return ans


print(get_closest(0, n-1))
