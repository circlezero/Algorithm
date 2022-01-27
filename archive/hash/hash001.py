import sys
from collections import Counter

input = sys.stdin.readline

def solution(a, b):
    temp = Counter(a) - Counter(b)
    for i in temp:
        res = i
    return res