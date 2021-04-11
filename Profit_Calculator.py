import time
exit = 0
def bc():
    total= {
        'cost_V':24.54,
        'sell_V':29.55,
        'ss':243
    }
    print('[Current]\n\ncost:', total['cost_V'], '\b$')
    print('sell price:', total['sell_V'], '\b$')
    print('Stock:', total['ss'])
    print(' \n\n')
    time.sleep(1)
    while True:
        while True:
            try:
                stock = int(input('Enter stock to be sold:'))
                total['ss'] = stock
                del stock
                time.sleep(0.4)
                break
            except ValueError:
                time.sleep(0.25)
                print('\n[Error]:\nenter a full number\n')
                time.sleep(0.5)
                continue
        while True:
            try:
                change = str(input('\nChange cost or sell value?(y/n):'))
                time.sleep(0.3)
                if change == 'y':
                    while True:
                        try:
                            c = float(input('\nNew cost per stock:'))
                            time.sleep(0.2)
                        except ValueError:
                            print('Enter a valid price (a real number)\n')
                            time.sleep(0.2)
                            continue
                        break
                    while True:
                        try:
                            d = float(input('New sell price per stock:'))
                            time.sleep(0.2)
                        except ValueError:
                            print('Enter a valid price (a real number)\n')
                            time.sleep(0.2)
                            continue
                        total['cost_V'] = c
                        total['sell_V'] = d
                        del change, c, d
                        break
                    break
                elif change == 'n':
                    time.sleep(1)
                    del change
                    break
                else:
                    print('I only understand yes or no ("y" or "n")')
                    continue
            except ValueError:
                print('Please use "y" for yes or "n" for no')
                time.sleep(0.3)
                continue

        print()
        print('calculating',end='\r')
        b = (total['sell_V']*total['ss'])-(total['cost_V']*total['ss'])
        time.sleep(0.2)
        print('calculating.',end='\r')
        c = round(b)
        time.sleep(0.2)
        print('calculating..',end='\r')
        c = int(c)
        time.sleep(0.2)
        print('calculating...\n')
        time.sleep(0.5)
        print('[Profit]\n\nGains:         ', c,'\b$\nAccurate Gains:', b,'\b$\n\n\n\n\n')
        inpt = str(input('Again?(y/n)'))
        if inpt == 'y':
            time.sleep(0.05)
            continue
        elif inpt == 'n':
            break
        else:
            print('Use "y" for yes and "n" for no')
            time.sleep(0.2)


def p():
    while True:
        while True:
            try:
                print()
                inpt = float(input('Input Money:'))
                break
            except ValueError:
                print('Invalid Input')
                time.sleep(0.1)
                continue
        print()
        print('[Converted]\n$%.2f' %(inpt))
        inpt = str(input('Again?(y/n)'))
        if inpt == 'y':
            time.sleep(0.05)
            continue
        elif inpt == 'n':
            break
        else:
            print('Use "y" for yes and "n" for no')
            time.sleep(0.2)


while True:
    if exit > 0:
        exit = 0
        break
    change = str(input('[Main Menu]\nBusinesss_Calculation[bc] or Payrolls[p]?:'))
    time.sleep(0.3)
    if change == 'bc':
        time.sleep(0.2)
        print('\nOpening Business Calculation [Task 1]\n\n')
        time.sleep(0.7)
        bc()#Opens business calculation
        while True:
            change = str(input('Exit[e] or Main Menu[mm]?'))
            print()
            if change == 'e':
                print('[Exitting]')
                time.sleep(1)
                exit = 1
                break
            elif change == 'mm':
                time.sleep(0.3)
                break
            else:
                print('Use "e" for Exit or "mm" for Main Menu')
                print()
                time.sleep(0.2)
                continue
    elif change == 'p':
        time.sleep(0.2)
        print('\nOpening Payrolls [Task 2]\n\n')
        time.sleep(0.7)
        p()#Opens payrolls
        while True:
            change = str(input('Exit[e] or Main Menu[mm]?'))
            print()
            if change == 'e':
                print('[Exitting]')
                time.sleep(1)
                exit = 1
                break
            elif change == 'mm':
                time.sleep(0.3)
                break
            else:
                print('Use "e" for Exit or "mm" for Main Menu')
                print()
                time.sleep(0.2)
                continue
    else:
        print('Can only receive Business_Calculation and Payrolls ("bc" or "p")\n')
        time.sleep(0.6)
        continue