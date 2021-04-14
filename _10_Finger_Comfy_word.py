import time
print('[Comfortable Word]')
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','w','v','y','x','z'}
aal = {'q','w','e','r','t','a','s','d','f','g','z','x','c','v','b'}
time.sleep(0.3)
def h():
    while True:
        a = str(input('\nPlease enter a word: '))
        a = set(a)
        c = a.difference(alphabet)
        c = bool(c)
        if c ==False:
            break
        else:
            time.sleep(0.1)
            print('Invalid. Try again.\n') 
            time.sleep(0.3)
            continue
    c = a.difference(aal)
    c = bool(c)
    if c == True:
        time.sleep(0.2)
        print('\n[Output]\n\n',c,'\n')
        time.sleep(0.2)
        print("You used both of your hands")
        time.sleep(0.2)
    else:
        time.sleep(0.2)
        print('\n[Output]\n\n',c,'\n')
        time.sleep(0.2)
        print("You didn't use both of your hands")
        time.sleep(0.2)
h()
while True:
    qui = False
    a = str(input('\nAgain?(y/n):'))
    if a == 'n':
        time.sleep(0.1)
        print('Quit')
        qui = True
    elif a == 'y':
        h()
    else:
        time.sleep(0.2)
        print('Error\n')
        h()
    if qui == True:
        break
    else:
        continue
#just copy paste and let it run