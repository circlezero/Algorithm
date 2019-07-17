import sys
maxIndex = 0
maxValue = 0    
for i in range(9):
    t = int(sys.stdin.readline())
    if t > maxValue:
        maxIndex = i+1
        maxValue = t

print(maxValue)
print(maxIndex)