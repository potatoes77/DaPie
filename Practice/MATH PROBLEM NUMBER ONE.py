#import pandas as pd

def DaMean(listOfNumbers):
    counter = 0
    currentNumber = int(listOfNumbers[0])
    while len(listOfNumbers) - 1 != counter:
        counter += 1
        currentNumber += int(listOfNumbers[counter])
    print(currentNumber)
    currentNumber /= counter + 1
    return currentNumber

def DaMAD(listOfNumbers, daNumber):
    counter = 0
    daNumber = daNumber
    while len(listOfNumbers) - 1 != counter:
        listOfNumbers[counter] -= daNumber
        listOfNumbers[counter] = abs(listOfNumbers[counter])
        counter += 1

    return DaMean(listOfNumbers)


listOfNumbers = [12, 1, 6, 10, 1, 2, 3, 10, 8, 3, 9, 8, 6, 8]
listOfNumbers2 = [11, 14, 11, 13, 6, 7, 8, 6, 8, 13, 8, 15, 13, 17, 15]
#series = pd.Series(listOfNumbers)
mean = DaMean(listOfNumbers)
mean2 = DaMean(listOfNumbers2)

print(mean)
print(mean2)







