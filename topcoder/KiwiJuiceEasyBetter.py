n = int(input())
capacilities = list(map(int, input().split()))
bottles = list(map(int, input().split()))

m = int(input())
fromId = list(map(int, input().split()))
toId = list(map(int, input().split()))

for i in range(m):
    f = fromId[i]
    t = toId[i]
    bottleSum = bottles[f] + bottles[t]
    bottles[t] = min(bottleSum, capacilities[t])
    bottles[f] = bottleSum - bottles[t]

print(' '.join(str(i) for i in bottles))