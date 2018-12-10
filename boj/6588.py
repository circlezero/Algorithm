MAX = 1000000
isPrime = [True] * (MAX+1)
primeList = []

for i in range(2, int(MAX**0.5)+1):
    if isPrime[i] == True:
        primeList.append(i)
        for j in range(i*i, MAX+1, i):
            isPrime[j] = False

def goldbach(n):
    msg = "Goldbach's conjecture is wrong."
    for i in primeList:
        if isPrime[n-i] == True and isPrime[i] == True:
            msg = f'{n} = {i} + {n-i}'
            break
    print(msg)

while True:
    n = int(input())
    if n is 0:
        break
    else:
        goldbach(n)