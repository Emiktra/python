#functions
def createList():
    listOfNumbers = []
    while True:
        inputNumber = input('A number for the list / press e to end  ')
        if inputNumber == 'e' or inputNumber == 'E' or inputNumber == 'End' or inputNumber == 'end':
            break
        elif inputNumber.isnumeric(): listOfNumbers.append(inputNumber)
    if listOfNumbers == []: listOfNumbers = [2, 1, 5, 7, 2, 0, 5]
    return listOfNumbers

def printMedian(listOfNumbers):
    from statistics import median
    empty = []
    for i in listOfNumbers:
        empty.append(i)
        print(sorted(empty, reverse=False))
        print(median(empty))

# flow
printMedian(createList())