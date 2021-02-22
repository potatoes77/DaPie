def VowelCounter(stringForFunction):
    counter = int()
    for letter in stringForFunction.upper():
        if letter == 'A':
            counter += 1
        if letter == 'E':
            counter += 1
        if letter == 'I':
            counter += 1
        if letter == 'O':
            counter += 1
        if letter == 'U':
            counter += 1
        if letter == 'Y':
            counter += 1
    print(counter)

VowelCounter('Kendrick Is The Best')
