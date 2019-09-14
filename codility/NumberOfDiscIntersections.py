## Solved on 2019.07.17 Reference https://www.martinkysel.com/codility-number-of-disc-intersections-2010-beta-solution/
import sys
A = list(map(int, sys.stdin.readline().split()))
ans = 0
B = []
for i, a in enumerate(A):
    B += [(i-a, True), (i+a, False)]
B.sort(key=lambda x: (x[0], not x[1]))

intersections, active_circles = 0, 0

for _, is_beginning in B:
    if is_beginning:
        intersections += active_circles
        active_circles += 1
    else:
        active_circles -= 1

    print(intersections, active_circles)
    if intersections > 10E6:
        ans = -1
        break
ans = intersections
print(ans)

## Tried 1 - Failed O(N ** 2)
##---

# def isIntersect(a, b):
#     for i in range(b-A[b], b+A[b]+1):
#         if a-A[a] <= i <= a+A[a]:
#             return True
#     return False

# for i in range(N):
#     for j in range(i+1, N):
#         if isIntersect(i, j):
#             ans += 1

# if ans >= 10000000:
#     ans = -1
# print(ans)

##---









