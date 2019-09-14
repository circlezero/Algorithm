def getStrInfo(S):
    alpha, number = 0, 0
    for i in S:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            alpha += 1
        elif '0' <= i <= '9':
            number += 1
        else:
            return (0, 0)
    return (alpha, number)


def solution(S):
    subStr = S.split(' ')
    ans = -1
    for i in subStr:
        a, n = getStrInfo(i)
        if a % 2 == 0 and n % 2 == 1:
            ans = max(len(i), ans)
    return ans


print(solution("test 5 a0A pass007 ?xy1"))
print(solution("zaq!2#edc"))
