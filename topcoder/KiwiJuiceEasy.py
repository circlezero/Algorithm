"""
n : 병의 수
capacilities : 병의 용량
bottles : 주스의 양

m : 조작 횟수
fromId : 옮길 주스 병의 Id
toId : 담길 주스의 Id
"""

n = int(input())
capacilities = list(map(int, input().split()))
bottles = list(map(int, input().split()))

m = int(input())
fromId = list(map(int, input().split()))
toId = list(map(int, input().split()))

for i in range(m):
    f = fromId[i]
    t = toId[i]
    if bottles[f] + bottles[t] > capacilities[t]:
        bottles[f] = bottles[f] - (capacilities[t] - bottles[t])
        bottles[t] = capacilities[t]
    else :
        bottles[t] = bottles[f] + bottles[t]
        bottles[f] = 0

print(' '.join(str(i) for i in bottles))