import time
startPoint = 0
finishPoint = 100


#changing default values
def changeValue():
    global startPoint
    global finishPoint
    while True:
        try:
            startPoint = int(input('start point (full number): '))
            break
        except ValueError:
            print('invalid')
            time.sleep(0.1)
    while True:
        try:
            finishPoint = int(input('finish point (full number): '))
            if len(range(startPoint, finishPoint)) > 10000:
                time.sleep(0.15)
                print('terminal can´t display that much\n' )
                continue
            if finishPoint <= startPoint: 
                print('finish point must be bigger than start point\n')
                continue
            print(f'\n[New {startPoint}-{finishPoint}]')
            time.sleep(0.5)
            break
        except ValueError:
            print('invalid')
            time.sleep(0.1)


#calculation part(math)
def calculate(start, finish):
    FizzBuzz = []
    for i in range(start, finish +1):
        if i%3 == 0 and i%5 == 0 and i !=0: FizzBuzz.append(f'{i} = FizzBuzz')
        elif i%3 == 0 and i !=0: FizzBuzz.append(f'{i} = Fizz')
        elif i%5 == 0 and i !=0: FizzBuzz.append(f'{i} = Buzz')
        else: FizzBuzz.append(i)
    print()
    print(*FizzBuzz, sep='\n')
    print()


#loop part(interface)
while True:
    startPoint = 0
    finishPoint = 100
    change = str(input('[Default is 0-100]\nchange starting and end point?(y/n)\t\t\t\t\t\t\t\tQuit?(q)\n'))
    if change == 'y': 
        changeValue()
        time.sleep(0.5)
        calculate(startPoint, finishPoint)
    elif change == 'n': calculate(startPoint, finishPoint)
    elif change == 'q': break
    else: 
        print('invalid\n')
        time.sleep(0.1)
        continue
