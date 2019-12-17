def solution(clothes):
    clothDict = {}
    clothTypes = []
    for cloth in clothes:
        clothTypes.append(cloth[1])
    clothTypes = list(set(clothTypes))

    for i in clothTypes:
        clothDict[i] = []

    for cloth in clothes:
        clothDict[cloth[1]].append(cloth[0])

    clothTypeNum = len(clothDict)
    clothNumArr = []
    for i in clothDict:
        clothNumArr.append(len(clothDict[i]))

    res = 1
    for i in clothNumArr:
        res = res * (i + 1)
    return res-1
