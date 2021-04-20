#tools, imports
import time
#variables
password = 'Ani85Mu4R3'
admin = 'Alexandra'
#functions
def change_username():
    while True:
        try:
            global admin
            admin = str(input('new username:'))
            admin = admin.lower().title()
            print(admin,'\n')
            time.sleep(1)
            break
        except ValueError:
            print('Use string')
            continue
def change_password():
    while True:
        try:
            global password
            password = str(input('new password:'))
            print(password,'\n')
            time.sleep(1)
            break
        except ValueError:
            print('Use string')
            continue
#loops
while True:
    print('Identity check, Enter Name:')
    name = str(input())
    if name.lower().title() == admin:
        print(f'Access Permitted: Hello {admin}')
        time.sleep(0.2)
        break
    else:
        print('Access Denied: try again')
        time.sleep(0.3)
        continue
while True:
    print(f"\n[{admin}]\npassword: {password}")
    print('\nChange Username(u) - Change Password(p) - Exit(e)')
    answer = input()
    time.sleep(0.2)
    if answer == 'u':
        change_username()
        continue
    elif answer == 'p':
        change_password()
        continue
    elif answer == 'e':
        print('exitting')
        break
    else:
        print('Invalid action; try again\n')
        continue