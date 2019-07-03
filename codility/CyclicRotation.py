import sys
from collections import deque
a = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
arr = deque(a)
arr.rotate(k)
print(list(arr))