def findWord(input1):
    input1 = input1.split(' ')
    longest = ""
    for word in input1:
        word = list(word)
        for i in range(0, len(word) -1):
            for e in range(i +1, len(word)):
                if word[i] == word[e]:
                    if "".join(word[i:e +1]) == "".join(reversed(word[i:e +1])) and len(word[i:e +1]) > len(longest):
                        longest = "".join(word[i:e +1])
                        break
    if len(longest) < 1: print("none")
    else: print("lonegst palindromic is", longest)

while True:
    input1 = input('Enter sentence/word:  ')
    if not input1:
        input1 = 'Hello thre ma man i dunno if there is any palagrams here but yeah banana'
    findWord(input1)