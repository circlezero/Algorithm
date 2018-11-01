for i in range(0,100): 
    try:
        print(input())
    except EOFError:
        break