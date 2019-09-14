def solution(A, B):
    ans = 0
    downFish = []
    for i in range(len(A)):
        if B[i] == 0:
            for d in downFish[::-1]:
                if d < A[i]:
                    downFish.pop()
                else:
                    break
            if not downFish:
                ans += 1
        elif B[i] == 1:
            downFish.append(A[i])
    ans += len(downFish)
    return ans