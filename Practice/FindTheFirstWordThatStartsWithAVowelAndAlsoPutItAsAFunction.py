
def RepetitiveAnalyzer(stringForFunction):
    counter = int(0)
    amazingLetter = ''
    if stringForFunction[counter].upper() == 'A':
        amazingLetter = stringForFunction[counter]
    if stringForFunction[counter].upper() == 'E':
        amazingLetter = stringForFunction[counter]
    if stringForFunction[counter].upper() == 'I':
        amazingLetter = stringForFunction[counter]
    if stringForFunction[counter].upper() == 'O':
        amazingLetter = stringForFunction[counter]
    if stringForFunction[counter].upper() == 'U':
        amazingLetter = stringForFunction[counter]
    if stringForFunction[counter].upper() == 'Y':
        amazingLetter = stringForFunction[counter]
    return amazingLetter

def FindTheFirstVowelThatStartsAWord(stringForFunction):
    counter = 0
    for letter in stringForFunction:
        if counter == 0:
            someVariable = RepetitiveAnalyzer(letter)
            if someVariable != '':
                break
        counter += 1
        if letter == ' ':
            someVariable = RepetitiveAnalyzer(stringForFunction[counter])
            if someVariable != '':
                break
    return someVariable


print(FindTheFirstVowelThatStartsAWord("How are you"))
print(FindTheFirstVowelThatStartsAWord("Are you stinky"))
print(sys.path)
