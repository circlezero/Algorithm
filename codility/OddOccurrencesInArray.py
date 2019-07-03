import sys
from collections import Counter
a = Counter(list(map(int, sys.stdin.readline().split())))
for i in a:
    if a[i] % 2 == 1:
        print(i)
        break