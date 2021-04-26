import time

def armstrong(nunber):
    abc = []
    summi = []
    nunber = str(nunber)
    for i in nunber:
        abc.append(int(i))
    for i in abc:
        summi.append(i**len(abc))
    result = sum(summi)
    nunber = int(nunber)
    if nunber == result:
        print(f'{nunber} is an Armstrong number')
        time.sleep(0.2)
    else:
        print(f'{nunber} is not an Armstrong number')
        time.sleep(0.2)

while True:
    nunber = input('enter a number: ')
    tt = nunber.isdigit()
    if tt == True:
        nunber = int(nunber)
    else:
        pass
    if tt == True and nunber > (-1):
        armstrong(nunber)
    else:
        print("""It is an invalid entry. Don't use non-numeric, float, or negative values!""")
        continue
    #repeat
    again = str(input("""Again?(y) or (n)\n"""))
    if again == 'y':
        time.sleep(0.2)
        continue
    else:
        print('exitting')
        time.sleep(0.2)
        break
    
