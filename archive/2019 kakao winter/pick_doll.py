basket = []


def stackDoll(num):
    res = 0
    if not basket:
        basket.append(num)
    elif basket[-1] == num:
        basket.pop()
        res = 2
    else:
        basket.append(num)
    return res


def pick(arr, col):
    res = 0
    leng = len(arr)
    for i in range(leng):
        num = arr[i][col]
        if num > 0:
            arr[i][col] = 0
            res = stackDoll(num)
            break
    return res


def solution(board, moves):
    answer = 0
    for i in moves:
        answer = answer + pick(board, i-1)
    return answer
