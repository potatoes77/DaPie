from unittest import TestCase

from DaMath import DaMath



class DaMedianTest(TestCase):
    def test_da_median(self):
        listOfNumbers = [4, 2, 3, 1]
        math = DaMath()
        result = math.DaMedian(listOfNumbers)
        print(result)

        listOfNumbers = [1,2,3,4]
        result = math.DaMedian(listOfNumbers)
        print(result)

        listOfNumbers = [2, 2, 2, 2]
        result = math.DaMedian(listOfNumbers)
        print(result)

        listOfNumbers = [2,3,4,6655, 0, 2, 3, 1]
        result = math.DaMedian(listOfNumbers)
        print(result)

    def test_da_mean(self):
        math = DaMath()
        listOfNumbers = [12, 1, 6, 10, 1, 2, 3, 10, 8, 3, 9, 8, 6, 8]
        result = math.DaMean(listOfNumbers)
        print(result)

    def test_da_MAD(self):
        math = DaMath()
        listOfNumbers = [12, 1, 6, 10, 1, 2, 3, 10, 8, 3, 9, 8, 6, 8]
        listOfNumbers2 = [11, 14, 11, 13, 6, 7, 8, 6, 8, 13, 8, 15, 13, 17, 15]
        result = math.DaMAD(listOfNumbers, listOfNumbers2)
        print(result)

    def test_da_range(self):
        math = DaMath()
        listOfNumbers = [7,6,4,8,6,5,3,2,9,1,10]
        result = math.DaRange(listOfNumbers)
        print(result)

    def test_da_quartile(self):
        math = DaMath()
        listOfNumbers = [5,7,4,4,6,2,8]
        result = math.DaQuartile(listOfNumbers)
        print(result)

    def test_da_IQR(self):
        math = DaMath()
        listOfNumbers = [5, 7, 4, 4, 6, 2, 8]
        result = math.DaIQR(listOfNumbers)
        print(result)

    def test_da_sample(self):
        math = DaMath()
        listOfNumbers = [1,2,3,4,5,6,7,8,9,10]
        result = math.DaSample(listOfNumbers, False, 4)
        print(result)
