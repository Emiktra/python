age =  True
chronic =  True
immune =True
while True:
    age = str(input('Are you a cigarette addict older than 75 years old?'))
    if age == 'yes':
        age = True
        break
    elif age == 'no':
        age = False
        break
    else:
        print('yes or no')
        continue
while True:
    chronic = str(input('Do you have a severe chronic disease?'))
    if chronic == 'yes':
        chronic = True
        break
    elif chronic == 'no':
        chronic = False
        break
    else:
        print('yes or no')
        continue
while True:
    immune = str(input('Is your immune system too weak?'))
    if immune == 'yes':
        immune = True
        break
    elif immune == 'no':
        immune = False
        break
    else:
        print('yes or no')
        continue
risk = (chronic or immune) and age
if risk == True:
    print("You are in risky group")
else:
    print('You are not in risky group')