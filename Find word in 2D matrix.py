def findWord(matrix, word):
    word = list(word)
    for i in matrix:
        for e in i:
            if e == word[0]:
                word.pop(0)
                if len(word) == 0:
                    return True
    if len(word) != 0:
        return False       
while True:
    matrix = input('Enter matrixes of characters:  ').upper()
    if not matrix:
        matrix = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
    word = input('Enter word to be found in metrixes:  ').upper()
    print(findWord(matrix, word))