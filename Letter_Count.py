while True:
    sentence = str(input('Enter a sentence: '))
    sentenceSet = set(sentence)
    listOfCount = {}
    for i in sentenceSet:
        listOfCount[i] = sentence.count(i)
    print(listOfCount, '\n')
    for i, b in zip(listOfCount.keys(), listOfCount.values()):
        print(f'{i} is used {b} times')
    print()