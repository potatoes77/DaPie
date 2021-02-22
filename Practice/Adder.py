class IKindaRememberAllOfIt:
    def RecursivePrint(self, HAHAHA):
        if 0 >= len(HAHAHA):
            return ""

        print(HAHAHA[0])


        return HAHAHA[0] + self.RecursivePrint(HAHAHA[1:])






    def CapCrusader(self, cap, crusaderThatIsKindaFat):
        if 0 >= len(crusaderThatIsKindaFat):
            return ""

        crusaderThatIsKindaFat = list(crusaderThatIsKindaFat)

        if cap == crusaderThatIsKindaFat[0]:
            crusaderThatIsKindaFat[0] = crusaderThatIsKindaFat[0].upper()

        print(crusaderThatIsKindaFat[0])

        return crusaderThatIsKindaFat[0] + self.CapCrusader(cap, crusaderThatIsKindaFat[1:])
