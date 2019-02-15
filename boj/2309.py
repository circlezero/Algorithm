heightList = []
for i in range(9):
    heightList.append(int(input()))

heightList.sort()
heightSum = sum(heightList)

removeElemOne = 0
removeElemTwo = 0

for i in range(9):
    for j in range(i+1, 9):
        if heightSum - (heightList[i] + heightList[j]) == 100:
            removeElemOne = heightList[i]
            removeElemTwo = heightList[j]
            break

heightList.remove(removeElemOne)
heightList.remove(removeElemTwo)

for i in heightList:
    print(i)