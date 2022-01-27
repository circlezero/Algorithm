from functools import cmp_to_key

def solution(A):
    ans = ''
    N = len(A)
    B = list(map(str, A))
    B.sort(key=cmp_to_key(lambda x, y: int(x+y)-int(y+x)), reverse=True)
    if ''.join(B) == ''.join(['0' for i in range(len(B))]):
        return '0'
    return ''.join(B)
    
print(solution([3, 30, 34, 5, 9]))