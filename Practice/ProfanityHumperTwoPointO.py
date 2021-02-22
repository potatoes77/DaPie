class ProfanityHumper:

    def Tracker(self):
        count = 0
        electroSet = set()
        while True:
            if self.IsCussWordTwoPointO():
                count += 1
                

    def GetTheInputFromTheUser(self):
        print("Gimme a sentence. NOW! NOW NOW NOW NOW NOW!")
        inputFromUser = input("Please give me a sentence with at least 1 cuss word here --> ")
        print(self.ReturnsAllTheWordsThatAreCussWords(inputFromUser))


    def IsCussWordTwoPointO(self, inputFromNOTNOTNOTUser):
        listOfShit = ['FUCK', 'SHIT', 'DICK', 'FRICK', 'FUCKITY', 'FUCKED', 'FUCKING', 'ASS']
        if inputFromNOTNOTNOTUser.upper() in listOfShit:

            return True

        return False

    def PutAsSentence(self, otherInput):
        if self.IsCussWordTwoPointO(otherInput):
            return '*' * len(otherInput) + ' '
        otherInput = otherInput + ' '
        return otherInput

    def SeeIfThereIsASpace(self, inputFromNOTNOTUser):
        if inputFromNOTNOTUser == ' ':
            return True

        return False

    def ReturnsAllTheWordsThatAreCussWords(self, inputFromANotUser):
        counter = 0
        allLetters = ''
        lengthOfString = len(inputFromANotUser)
        sentence = ''
        while counter < lengthOfString:
            if counter == 0:
                while inputFromANotUser[counter] != ' ':
                    allLetters += inputFromANotUser[counter]
                    counter += 1
                sentence += self.PutAsSentence(allLetters)
                allLetters = ''


            if self.SeeIfThereIsASpace(inputFromANotUser[counter]):
                counter += 1
                while inputFromANotUser[counter] != ' ':
                    allLetters += inputFromANotUser[counter]
                    if counter == lengthOfString - 1:
                        sentence += self.PutAsSentence(allLetters)

                        return sentence


                    counter += 1
                sentence += self.PutAsSentence(allLetters)
                allLetters = ''

            elif not self.SeeIfThereIsASpace(inputFromANotUser[counter]):
                counter += 1

        return sentence
