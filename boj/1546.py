n = int(input())
subjects = sorted(list(map(int, input().split())), reverse=True)
newSum = 0
for i in subjects:
    newSum += (i/subjects[0] * 100)
print('{:.2f}'.format(newSum / len(subjects)))