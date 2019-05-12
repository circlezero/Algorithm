import sys
n, m = map(int, sys.stdin.readline().split())

color = [[0 for i in range(m+1)] for j in range(n+1)]

def ConvertASCII(R, G, B):
    intensity = 2126 * R + 7152 * G + 722 * B
    asciiCode = 46
    if 0 <= intensity < 510000:
        asciiCode = 35
    elif 510000 <= intensity < 1020000:
        asciiCode = 111
    elif 1020000 <= intensity < 1530000:
        asciiCode = 43
    elif 1530000 <= intensity < 2040000:
        asciiCode = 45
    return asciiCode

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        color[i][j] = ConvertASCII(a[3*j], a[3*j+1], a[3*j+2])
for i in range(n):
    for j in range(m):
        print(chr(color[i][j]), end="")
    print()
