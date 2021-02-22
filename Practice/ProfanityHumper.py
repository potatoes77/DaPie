class ProfanityHumper:
    def IsCussWordTwoPointO(self, inputFromNOTNOTNOTUser):
        listOfShit = ['FUCK', 'SHIT', 'DICK-SUCKING-DUMB-ASS-LITTLE-BAG-OF-SHIT-FUCK']
        if inputFromNOTNOTNOTUser.upper() in listOfShit:
            return True


        return False

    def SeeIfThereIsASpace(self, inputFromNOTNOTUser):
        if inputFromNOTNOTUser == ' ':
            return True


        return False

    def ReturnsAllTheWordsThatAreCussWords(self, inputFromUser):
        counter = 0
        allLetters = ''
        allCussWords = list()
        lengthOfString = len(inputFromUser)
        while counter < len(inputFromUser):
            if counter == 0:
                while inputFromUser[counter] != ' ':
                    allLetters += inputFromUser[counter]
                    counter += 1
                if self.IsCussWordTwoPointO(allLetters):
                    allCussWords.append(allLetters)
                    allLetters = ''

            if self.SeeIfThereIsASpace(inputFromUser[counter]):
                counter += 1
                while inputFromUser[counter] != ' ':
                    allLetters += inputFromUser[counter]
                    if counter == lengthOfString - 1:
                        if self.IsCussWordTwoPointO(allLetters):
                            allCussWords.append(allLetters)


                            return allCussWords
                        else:


                            return allCussWords
                    counter += 1
                if self.IsCussWordTwoPointO(allLetters):
                    allCussWords.append(allLetters)
                    allLetters = ''
                allLetters = ''

            elif not self.SeeIfThereIsASpace(inputFromUser[counter]):
                counter += 1


        return allCussWords
