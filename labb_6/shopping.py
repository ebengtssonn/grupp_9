class Shopping:
    def __init__(self, namn, antal, pris):
        self.__namn = namn
        self.__antal = antal
        self.__pris = pris

    def setNamn(self, namn):
        self.__namn = namn
    
    def setAntal(self, antal):
        self.__antal = antal
    
    def setPris(self, pris):
        self.__pris = pris

    def getNamn(self):
        return self.__namn
    
    def getAntal(self):
        return self.__antal

    def getPris(self):
        return self.__pris

    def __str__(self):
        utskrift = 'Namn på vara:' +self.getNamn()+  \
             '\nAntal:' +str(self.getAntal())+  \
                 ' \nPris:' +str(self.getPris())
        return utskrift
