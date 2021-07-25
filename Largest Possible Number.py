def createList():
    listOfNumbers = []
    while True:
        inputNumber = input('A number for the list / press e to end  ')
        if inputNumber == 'e' or inputNumber == 'E' or inputNumber == 'End' or inputNumber == 'end':
            break
        elif int(inputNumber): listOfNumbers.append(int(inputNumber))
    if not bool(listOfNumbers): return [34, 55, 324, 5, 0.23]
    return list(map(abs, listOfNumbers))

def FindLargest(listOfNumbers):
    listOfNumbers.sort()
    print(listOfNumbers[-1]*listOfNumbers[-2]*listOfNumbers[-3])

#flow
while True: 
    FindLargest(createList())