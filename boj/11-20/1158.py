import sys
import collections
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]
q = collections.deque(arr)
res = []
while q:
    q.rotate(-k+1)
    res.append(q.popleft())
print(f'<{", ".join(res)}>')
