import random

class DaMath:


    def DaMean(self, listOfNumbers):
        counter = 0
        currentNumber = int(listOfNumbers[0])
        while len(listOfNumbers) - 1 != counter:
            counter += 1
            currentNumber += int(listOfNumbers[counter])
        print(currentNumber)
        currentNumber /= counter + 1
        return currentNumber


    def DaMAD(self, listOfNumbers, daNumber):
        counter = 0
        daNumber = daNumber
        while len(listOfNumbers) - 1 != counter:
            listOfNumbers[counter] -= daNumber
            listOfNumbers[counter] = abs(listOfNumbers[counter])
            counter += 1

        return self.DaMean(listOfNumbers)

    def DaMedian(self, listOfNumbers):

        length = len(listOfNumbers)
        listofnumbers2 = sorted(listOfNumbers)
        if length % 2 == 0:
            length1 = int(length / 2 - 1)
            length2 = int(length / 2)
            middleNumber = listofnumbers2[length1]
            middleNumber2 = listofnumbers2[length2]
            middleSolution = middleNumber + middleNumber2
            return middleSolution / 2

        else:
            length2 = int(length/2)
            numberInMiddle = listofnumbers2[length2]
            finalNumberInMiddle = numberInMiddle
            return finalNumberInMiddle

    def DaRange(self, listOfNumbers):
        length = len(listOfNumbers) - 1
        sortedListOfNumbers = sorted(listOfNumbers)
        smallestNumber = sortedListOfNumbers[0]
        largestNumber = sortedListOfNumbers[length]
        finalNumber = largestNumber - smallestNumber
        return finalNumber

    def FindAllTheNumbersThatAreLessThanACertainNumber(self, median, listOfNumbers):
        counter = 0
        newListOfNumbers = []
        while counter < len(listOfNumbers):
            if listOfNumbers[counter] < median:
                newListOfNumbers.append(listOfNumbers[counter])
            counter += 1
        return newListOfNumbers

    def FindAllTheNumbersThatAreMoreThanACertainNumber(self, median, listOfNumbers):
        counter = 0
        newListOfNumbers = []
        while counter < len(listOfNumbers):
            if listOfNumbers[counter] > median:
                newListOfNumbers.append(listOfNumbers[counter])
            counter += 1
        return newListOfNumbers

    def DaQuartile(self, listOfNumbers):
        median = self.DaMedian(listOfNumbers)
        bottomQuartile = self.FindAllTheNumbersThatAreLessThanACertainNumber(median, listOfNumbers)
        upperQuartile = self.FindAllTheNumbersThatAreMoreThanACertainNumber(median, listOfNumbers)
        lowerQuartileTwoPointOh = self.DaMedian(bottomQuartile)
        upperQuartileTwoPointOh = self.DaMedian(upperQuartile)
        return lowerQuartileTwoPointOh, upperQuartileTwoPointOh

    def DaIQR(self, listOfNumbers):
        lowerQuartile = self.DaQuartile(listOfNumbers)[0]
        upperQuartile = self.DaQuartile(listOfNumbers)[1]
        IQR = upperQuartile - lowerQuartile
        return IQR

    def DaSample(self, listOfNumbers, isHat, sizeOfSample):
        isHatFalseTrue = isHat
        sample = []
        counter = 0
        if isHatFalseTrue == True:
            while counter < sizeOfSample:
                randomIndex = random.randint(0,len(listOfNumbers) - 1)
                sample.append(listOfNumbers[randomIndex])
                counter += 1
            return sorted(sample)
        if isHatFalseTrue == False:
            while counter < sizeOfSample:
                randomIndex = random.randint(0,len(listOfNumbers) - 1)
                sample.append(listOfNumbers[randomIndex])
                del listOfNumbers[randomIndex]
                counter += 1
            return sorted(sample)


