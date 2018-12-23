import sys
import collections

n,m = sys.stdin.readline().strip().split()
m = int(m)
q = collections.deque()
for i in range(1, int(n)+1):
    q.appendleft(str(i))

a = []
while len(q) > 0:
    q.rotate(m)
    a.append(q.popleft())

print(f'<{", ".join(a)}>')