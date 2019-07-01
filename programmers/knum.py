import sys
def solution(array, commands):
    answer = []
    for a in commands:
        new_arr = array[a[0]-1:a[1]]
        new_arr.sort()
        answer.append(new_arr[a[2]-1])
    return answer