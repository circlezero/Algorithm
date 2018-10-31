for i in range(0,100): 
    try:
        a = input()
        if a == '':
            break
        print(a)
    except EOFError:
        break