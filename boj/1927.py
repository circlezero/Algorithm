import sys
import heapq
input = sys.stdin.readline
n = int(input())
a = []
heapq.heapify(a)
for i in range(n):
    x = int(input())
    if x == 0:
        if not a:
            print(0)
        else:
            print(heapq.heappop(a))
    else:
        heapq.heappush(a, x)
