from math import sqrt
def solution(N):
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return int(2*(i+N/i))

print(solution(30))
print(solution(36))