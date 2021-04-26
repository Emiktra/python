import time

def alibaba(PrimeNumber):
    for i in range(2, PrimeNumber):
        xx = PrimeNumber / i
        xxx = xx.is_integer()
        if xxx == True or PrimeNumber == 1:
            print(f'{PrimeNumber} is not a prime number\n\n')
            break
        else:
            print(f'{PrimeNumber} is a prime number\n\n')
            break   

while True:
    try:
        PrimeNumber = int(input('Enter a number: '))
        if PrimeNumber < 1:
            print('enter a positive number\n')
            time.sleep(0.2)
            continue
        alibaba(PrimeNumber)
        continue
    except ValueError:
        print('enter an integer\n')
        time.sleep(0.2)
        continue
