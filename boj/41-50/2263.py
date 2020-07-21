import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
position = [0] * (n + 1)

for i in range(n):
    position[in_order[i]] = i


def find_pre(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    print(root, end=' ')
    p = position[root]
    left = p - in_start

    find_pre(in_start, p - 1, post_start, post_start + left-1)
    find_pre(p+1, in_end, post_start + left, post_end-1)


find_pre(0, n-1, 0, n-1)
