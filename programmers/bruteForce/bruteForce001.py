def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    countArr = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == num1[i%5]:
            countArr[0] += 1
        if answers[i] == num2[i%8]:
            countArr[1] += 1
        if answers[i] == num3[i%10]:
            countArr[2] += 1

    maxVal = max(countArr)
    answer = []
    for i in range(3):
        if maxVal == countArr[i]:
            answer.append(i+1)
    return answer