# ReverseString

def ReverseString(x):
    index = len(x) - 1
    allLetters = ""
    for letter in x:
        singleLetter = x[index]
        print(singleLetter)
        index -= 1
        allLetters += singleLetter
    return allLetters

print(ReverseString("level"))
