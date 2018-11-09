array = [0]*10000

def self_number(num):
    t = num
    next_num = t
    while t >= 10:
        next_num += (t % 10)
        t = int(t/10)
    next_num += t

    if next_num < 10000 and array[next_num] == 0:
        array[next_num] = 1
        self_number(next_num)
    return

for i in range(1, 10000):
    if array[i] == 1: continue
    self_number(i)

for i in range(1, 10000):
    if array[i] == 0: print(i)