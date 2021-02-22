def SuperIndex(stringForFunction, letterInString):
    index = int(0)
    for x in stringForFunction.upper():
        if x == letterInString.upper():
            print(x)
            print(index + 1)
            break
        index += 1


SuperIndex('Onomatopoiea', 't')
