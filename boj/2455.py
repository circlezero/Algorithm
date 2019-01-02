max = 0
people_num = 0
for i in range(4):
    people_out, people_in = list(map(int, input().split()))
    people_num -= people_out
    if people_num > max:
        max = people_num
    people_num += people_in
    if people_num > max:
        max = people_num
print(max)
