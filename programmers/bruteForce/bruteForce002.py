from itertools import permutations 
import math
def isPrime(num):
    if num == 0 or num == 1: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    ansArr = []
    for i in range(1, len(numbers)+1):
        perm = permutations(numbers, i)
        for j in set(perm):
            num = int(''.join(list(j)))
            if isPrime(num):
                ansArr.append(num)

    answer = len(list(set(ansArr)))

    return answer