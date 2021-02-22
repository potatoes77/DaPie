class VowelHumper:
    def RepetitiveAnalyzer(self, stringForFunction):
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

    def FindTheFirstVowelThatStartsAWord(self, stringForFunction):
        someVariable = ''
        counter = 0
        for letter in stringForFunction:
            if counter == 0:
                someVariable = self.RepetitiveAnalyzer(letter)
                if someVariable != '':
                    break
            counter += 1
            if letter == ' ':
                someVariable = self.RepetitiveAnalyzer(stringForFunction[counter])
                if someVariable != '':
                    break
        return someVariable

    def PrintsTheFirstWordThatStartsWithAVowel(self, sentence):
        allLetters = ''
        counter = 0
        for otherLetter in sentence:
            if counter == 0:
                if otherLetter.upper() == 'A' or otherLetter.upper() == 'E' or otherLetter.upper() == 'I' \
                        or otherLetter.upper() == 'O' or otherLetter.upper() == 'U' or otherLetter.upper() == 'Y':
                    allLetters += otherLetter
                    for otherOtherOtherLetter in sentence:
                        counter += 1
                        if sentence[counter] == ' ':
                            return allLetters
                        allLetters += sentence[counter]




            elif otherLetter == ' ':
                if sentence[counter + 1].upper() == 'A' or sentence[counter + 1].upper() == 'E' \
                        or sentence[counter + 1].upper() == 'I' or sentence[counter + 1].upper() == 'O' \
                        or sentence[counter + 1].upper() == 'U' or sentence[counter + 1].upper() == 'Y':
                    counter = counter + 1
                    allLetters += sentence[counter]
                    for otherOtherLetter in sentence:
                        counter += 1
                        if sentence[counter] == ' ':
                            return allLetters
                        allLetters += sentence[counter]
            counter += 1

        return None

    def SeeIfTheFirstLetterIsAVowel(self, singleLetter):
        if 'A' == singleLetter.upper() or 'E' == singleLetter.upper() or 'I' == singleLetter.upper() \
                or 'O' == singleLetter.upper() or 'U' == singleLetter.upper() or 'Y' == singleLetter.upper():
            return True

        return False

    def SeeIfThereIsASpace(self, singleLetter):
        if singleLetter == ' ':
            return True

        return False

    def FindsAllTheWordsThatStartsWithAVowelAndAlsoPutItAsAListAndFunction(self, sentence):
        counter = int(0)
        allLetters = str()
        allWords = list()
        for letter in sentence:
            if counter == 0:
                if self.SeeIfTheFirstLetterIsAVowel(letter):
                    allLetters += sentence[0]
                    for otherLetter in sentence:
                        counter += 1
                        if self.SeeIfThereIsASpace(sentence[counter]):
                            allWords.append(allLetters)
                            allLetters = str()
                            break
                        allLetters += sentence[counter]

            if self.SeeIfThereIsASpace(sentence[counter]):
                if self.SeeIfTheFirstLetterIsAVowel(sentence[counter + 1]):
                    for otherOtherLetter in sentence:
                        counter += 1
                        if self.SeeIfThereIsASpace(sentence[counter]):
                            allWords.append(allLetters)
                            allLetters = str()
                            break
                        if counter == len(sentence) - 1:
                            allWords.append(allLetters + sentence[len(sentence) - 1])
                            return allWords
                        allLetters += sentence[counter]

            counter += 1
            if counter == len(sentence) - 1:
                return allWords



        return allWords

# def WhatIsAListPretendThatThisIsAQuestionMark(self):
#      test = list()
#      bla = 'bla bla bla'
#      test.append(bla)
#     print("tst = " + test[0])
# See if the first letter of the first word is a vowel. <-- Function v/
# Make main function that does all the hard stuff and build functions along the way.
# Make sure to put other functions above the main function which is
# FindsAllTheWordsThatStartsWithAVowelAndAlsoPutItAsAListAndFunction.
# Rename VowelHelper to VowelHumper :D LOLLLLLLL XD SO FUNNY HAHAHHA HILARIOUS XD LOLLLLLLL
