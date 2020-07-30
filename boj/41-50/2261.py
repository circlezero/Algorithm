import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
a.sort()


def get_dist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def get_closest(x,  y):
    n = y - x
    if n == 1:
        return 0
    elif n == 2:
        return get_dist(a[x], a[x+1])
    elif n == 3:
        return min(get_dist(a[x], a[x+1]), get_dist(a[x+1], a[x+2]), get_dist(a[x], a[x+2]))

    ind = (x+y) // 2
    ans = min(get_closest(x, ind), get_closest(ind, y))
    mid = a[ind][0]
    b = []
    for i in range(x, y):
        if (mid - a[i][0])**2 <= ans:
            b.append(a[i])
    b.sort(key=lambda x: x[1])

    leng = len(b)
    for i in range(leng-1):
        for j in range(i+1, leng):
            if (b[j][1] - b[i][1])**2 >= ans:
                break
            elif b[i][0] < mid and b[j][0] < mid:
                continue
            elif b[i][0] > mid and b[j][0] > mid:
                continue
            ans = min(ans, get_dist(b[i], b[j]))
    return ans


print(get_closest(0, n))
