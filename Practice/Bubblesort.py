class Bubblesort:


    def Bubblesort(self, listOfNumbers):
        counter = 0
        numberHolder = ''
        numberHolder2 = ''
        didSwitch = False
        while counter < len(listOfNumbers) - 1:
            #print(listOfNumbers)
            if int(listOfNumbers[counter]) > int(listOfNumbers[counter + 1]):
                numberHolder = listOfNumbers[counter]
                numberHolder2 = listOfNumbers[counter + 1]
                listOfNumbers[counter + 1] = numberHolder
                listOfNumbers[counter] = numberHolder2
                didSwitch = True



            counter += 1
            print(listOfNumbers)



        if didSwitch == False:
            return listOfNumbers
        if didSwitch == True:
            self.Bubblesort(listOfNumbers)



