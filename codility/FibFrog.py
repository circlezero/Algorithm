def solution(A):
    A.append(1)
    L = len(A)
    max_idx = 0

    # 피보나치 배열 생성
    fibo = [0,1]+[0] * 100
    for i in range(2, 100):
        fibo[i] = fibo[i-1] + fibo[i-2]
        if fibo[i] > L:
            max_idx = i
            break

    # 점프가 가능한 잎의 배열
    jumpable = [-1] * L
    for i in fibo[2:max_idx]:
        if A[i-1] == 1:
            jumpable[i-1] = 1


    for i in range(L):
        if A[i] == 0 or jumpable[i] == 1:
            continue
    
        min_ind = -1
        min_value = 100000
        
        for j in fibo[2:max_idx]:
            prev = i - j
            if prev < 0:
                break
            if jumpable[prev] > 0 and min_value > jumpable[prev]:
                min_value = jumpable[prev]
                min_ind = prev
        if min_ind != -1:
            jumpable[i] = min_value + 1
    return jumpable[L-1]

print(solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0] ))
# print(solution([0, 0, 0]))
# print(solution([1, 1, 0, 0, 0]))