"""
n : 친구들이 수
fisrt : 친구들이 좋아하는 첫 번째 주제
second : 친구들이 좋아하는 두 번째 주제
"""

n = int(input())
first = input().split()
second = input().split()
topic = {}
result = 0

for i in range(n):
    topic[first[i]] = 0
    topic[second[i]] = 0

for i in range(n):
    topic[first[i]] += 1
    topic[second[i]] += 1

for i in topic:
    if result < topic[i]:
        result = topic[i]

print(result)