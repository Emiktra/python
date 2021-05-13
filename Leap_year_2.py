import time

def calculation(a):
    if a % 4 != 0: return False
    if a % 100 == 0 and a % 400 != 0: return False
    return True
while True:
    try:
        inputt = int(input('Please enter a full year: '))
        if calculation(inputt) == False: print(inputt, 'is not a leap year\n')
        if calculation(inputt) == True: print(inputt, 'is a leap year\n')
    except ValueError:
        print('enter full year (int)\n')
        time.sleep(0.1)
        continue