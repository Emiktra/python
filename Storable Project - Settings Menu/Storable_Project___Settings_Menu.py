import time

#functions
settings = {}
def option_load():
    global settings
    with open('settings.txt', 'r', encoding='utf-8') as file:
        for i in file:
            option, value = i.partition('=')[::2]
            settings[option.strip()] = value.strip()
        if settings == False: print('[Settings is Empty]')
        for i in list(settings.keys()):
            if len(i) < 4: del i 
def option_save():
    global settings
    with open('settings.txt', 'w', encoding='utf-8') as file:
        for i, e in zip(settings.keys(), settings.values()):
            file.write(str(i) + ' = ' + str(e) + '\n')
def option_display():
    for i, e in zip(settings.keys(), settings.values()):
        print('[{: ^15}]'.format(i), ' '*11, e)
def option_change_or_switch():
    while True:
        inputt = str(input('\nadd/remove options?(y/n)'))
        if inputt.lower() == 'n' or inputt.lower() == 'no': 
            time.sleep(0.1)
            break
        elif inputt.lower() == 'y' or inputt.lower() == 'ye' or inputt.lower() == 'yes': 
            option_edit()
            time.sleep(0.1)
        else: 
            print('invalid answer')
            time.sleep(0.1)
def option_edit():
    while True:
        inputt = str(input('add/remove or end?(a/r/e)'))
        if inputt.lower() == 'a' or inputt.lower() == 'add': option_add()
        elif inputt.lower() == 'r' or inputt.lower() == 'remove': 
            if settings == False: print('Nothing to remove')
            else: option_remove()
        elif inputt.lower() == 'e' or inputt.lower() == 'end': break
        else: print('invalid')
def option_remove():
    global settings
    for i in settings.keys():
        print('[{: ^15}]'.format(i), 'keyword =', i.lower()[:3])
    print()
    while True:
        answer = str(input('Enter the keyword of the option you want to delete. If more than one, enter full name. Press "c" to cancel.(c)'))
        a = len(settings)
        if answer.lower() == 'c' or answer == 'cancel': break
        for i in list(settings.keys()): 
            if answer.lower() == i.lower(): settings.pop(i)
        for i in list(settings.keys()):
            if answer.lower() == i.lower()[:3]: settings.pop(i)
        if a == len(settings): print('invalid or none existent')
        del a
def option_add():
    global settings
    while True:
        answer = str(input('Enter the name of the setting. It may not be longer than 15. Press "e" to end: '))
        if answer == 'e' or answer == 'en' or answer == 'end': break
        elif len(answer) > 15: print("The name can't contain more than 15 letters")
        elif len(answer) < 3: print("The name can't be shorter than 3 letters")
        if answer == 'cancel' or answer == 'end': print("can't use command words") 
        else: settings[answer] = 1
def option_parameters():
    while True:
        inputt = str(input('Edit settings?(y/n)'))
        if inputt.lower() == 'n' or inputt.lower() == 'no': 
            time.sleep(0.1)
            break
        elif inputt.lower() == 'y' or inputt.lower() == 'ye' or inputt.lower() == 'yes': 
            option_changes()
            time.sleep(0.1)
        else: print('invalid\n')
        for i, e in zip(settings.keys(), settings.values()):
            print('[{: ^15}]'.format(i), ' '*11, e)
def option_changes():
    global settings
    for i, e in zip(settings.keys(), settings.values()):
            print('[{: ^15}]'.format(i) + i.lower()[:3], '  =', e)
    while True:
        answer = str(input('Enter the name/keyword of the setting to change. "c" to cancel: '))
        if answer == 'c' or answer == 'cancel': break
        for i in list(settings.keys()): 
            if answer.lower() == i.lower(): 
                acdd = str(input('\n[{: ^15}]'.format(i) + ' = '))
                settings[i] = acdd
                continue
        for i in list(settings.keys()):
            if answer.lower() == i.lower()[:3]:  
                acdd = str(input('\n[{: ^15}]'.format(i) + ' = '))
                settings[i] = acdd

#program flow
option_load()

option_display()
option_change_or_switch()
option_parameters()

option_save()