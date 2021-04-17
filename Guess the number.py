import random
import time
print('''Let's play a game called guess the number in my mind (1-1000)''')
rando = random.randint(1, 1001)
while True:
    x = int(input('''Enter the number I'm guessing:'''))
    if x > rando:
        print('a little lower')
    elif x < rando:
        print('a little higher')
    else:
        print('You found it!')
        time.sleep(1)
        break
