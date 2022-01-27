import sys
input = sys.stdin.readline

N, B = input().split()


def convertNtoTen(N, B):
    res = 0
    for ind, val in enumerate(N[::-1]):
        n = ord(val) - ord('0')
        if 'A' <= val <= 'Z':
            n = ord(val) - ord('A') + 10
        res += n * pow(int(B), ind)
    return res


print(convertNtoTen(N, B))
