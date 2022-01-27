import sys
input = sys.stdin.readline

MAX_NUM = 1_000_000
PRIME = [1] * MAX_NUM + [1]
PRIME[0] = 0
PRIME[1] = 0
i = 2
primeList = []
while i * i <= MAX_NUM:
    if PRIME[i] == 1:
        primeList.append(i)
        for j in range(i*i, MAX_NUM+1, i):
            PRIME[j] = 0
    i += 1


def find_goldbach(n):
    msg = "Goldbach's conjecture is wrong."
    for i in primeList:
        if PRIME[n-i] == 1 and PRIME[i] == 1:
            msg = f'{n} = {i} + {n-i}'
            break
    print(msg)


while True:
    n = int(input())
    if n == 0:
        break
    find_goldbach(n)
