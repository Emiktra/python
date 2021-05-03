import time
PrimeList = []
#identification part
while True:
    try:
        EnteredLimit = int(input('Enter the limit for calculating prime numbers: '))
        if not EnteredLimit < 2: break
        print('enter a value bigger than 1')
        time.sleep(0.1)
        continue
    except ValueError:
        print('enter a full number...\n')
        time.sleep(0.1)
        continue
#calculation part
for i in range(2, EnteredLimit +1):
    key = False
    for e in range(2, i):
        if i%e == 0:
            key = True
            break
    if key == True: pass
    if key == False: PrimeList.append(i) 
print(PrimeList)