n = int(input())

cycle = 0
t = n
while True:
    a = int(t / 10)
    b = t % 10
    t = b*10 + ((a+b)%10)
    cycle += 1
    if t == n: break
print(cycle)