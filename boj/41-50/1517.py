import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = [0] * 500000


def merge_sort(start, end):
    if start == end:
        return 0

    mid = (start + end) // 2
    ans = merge_sort(start, mid) + merge_sort(mid+1, end)

    i = start
    j = mid + 1
    k = 0

    while i <= mid or j <= end:
        if i <= mid and (j > end or a[i] <= a[j]):
            b[k] = a[i]
            k += 1
            i += 1
        else:
            ans += (mid-i+1)
            b[k] = a[j]
            k += 1
            j += 1

    for i in range(start, end+1):
        a[i] = b[i-start]

    return ans


res = merge_sort(0, n-1)
print(res)
