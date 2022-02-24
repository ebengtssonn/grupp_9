class Shopping: # Skapar klassen shopping.
     
    def __init__(self, namn, antal, pris): #Definerar konstruktor.
        #Definerar privata instansvariablerna namn, antal och pris.
        self.__namn = namn
        self.__antal = antal
        self.__pris = pris
#Definerar set- och getmetoder. 
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

    def __str__(self):#Definerar str metod för utskrift.
        utskrift = 'Namn på vara: ' +self.getNamn()+  \
             '\nAntal: ' +str(self.getAntal())+  \
                 ' \nPris: ' +str(self.getPris())#Typar om antal och pris till sträng.
        return utskrift
