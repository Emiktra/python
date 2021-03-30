import time
while True:
    try:
        x = int(input('Please enter a 4 digit year:'))
        if x > 999 and x < 9999:
            break
        else:
            time.sleep(0.2)
            print('Enter 4 digits: ____')
            time.sleep(0.55)
            continue
    except ValueError:
            time.sleep(0.2)
            print('Enter a full whole number : ____\n')
            time.sleep(0.55)
            continue
y = x % 4
if y != 0:
    y = 'False'
else:
    y = 'True'
time.sleep(0.2)
print('\n[Notice]\n If the year', x, 'is a leap year, it will output True. Else it will output False')
time.sleep(0.6)
print('\nOUTPUT:\n', y)