def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

def solution(N, M):
    ans = N // gcd(N,M)
    return ans

print(solution(10, 4))