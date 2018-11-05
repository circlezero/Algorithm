a, b = input().split()
sum = int(b)
for i in range(1, int(a)):
    # if( int(a) == 1 ): break
    if( i == 4 or i == 6 or i == 9 or i == 11 ): sum += 30
    elif(i == 2): sum += 28
    else: sum += 31
        
sum = sum % 7
if sum == 0: print('SUN')
elif sum == 1: print('MON')
elif sum == 2: print('TUE')
elif sum == 3: print('WED')
elif sum == 4: print('THU')
elif sum == 5: print('FRI')
elif sum == 6: print('SAT')