#set both one to 1, rest to 0
#while loop:
#   add the two variables
#   set new variable to the sum
#   set first_variable to second_variable
#   set second_variable to new_variable
#   break from loop if the new variable is bigger than 55
#   add the new variable to a list
def unefficient_way():
    ffibonaci = []
    a, b, c = 1, 0, 0
    while True:
        c = a + b
        a = b
        b = c
        if c > 55:
            break
        ffibonaci.append(c)
    print('\nfibonacci →',ffibonaci)

#create a list [1, 1]
#while loop:
#   assign new variable the sum of index -1 and index -2
#   add the new variable to the end of the list
#   break from loop if index -1 is bigger than 55

def efficient_way():
    fibonacci = [1, 1]
    while True:
        new = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(new)
        if fibonacci[-1] > 54:
            break
    print('\nfibonacci →',fibonacci)

while True:
    answer = str(input('efficient version or unefficient version? ("ef" or "uf") :  '))
    if answer == "ef":
        efficient_way()
    elif answer == "uf":
        unefficient_way()
    else:
        print('"ef" for efficient or "uf" for unefficient code')