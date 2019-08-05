from math import sqrt

def solution(N, P, Q):    
    prime_table = [False, False] + [True] * (N-1)
    prime = []
    cnt = 0

    for element in range(2, int(sqrt(N))+1):
        if prime_table[element] == True:
            prime.append(element)
            cnt += 1
            multiple = element * element
            while multiple <= N:
                prime_table[multiple] = False
                multiple += element
    
    for element in range(int(sqrt(N))+1, N+1):
        if prime_table[element] == True:
            prime.append(element)
            cnt += 1
    
    semiprime = [0] * (N+1)
    for i in range(cnt-1):
        for j in range(i, cnt):
            if prime[i]*prime[j] > N:
                break
            semiprime[prime[i]*prime[j]] = 1
    
    for i in range(1, N+1):
        semiprime[i] += semiprime[i-1]
    
    M = len(P)
    result = []
    for i in range(M):
        result.append(semiprime[Q[i]] - semiprime[P[i]-1])
    return result