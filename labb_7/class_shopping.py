class Shopping: # Skapar klassen shopping.
     
    def __init__(self, namn, antal, pris): #Definerar konstruktor.
        #Definerar privata instansvariablerna namn, antal och pris.
        self.__namn = namn
        self.__antal = antal
        self.__pris = pris
        
    #Definerar set- och getmetoder. 
    def set_namn(self, namn):
        self.__namn = namn
    
    def set_antal(self, antal):
        self.__antal = antal
    
    def set_pris(self, pris):
        self.__pris = pris

    def get_namn(self):
        return self.__namn
    
    def get_antal(self):
        return self.__antal

    def get_pris(self):
        return self.__pris

    def __str__(self):#Definerar str metod för utskrift.
        utskrift = 'Namn på vara: ' +self.get_namn()+  \
             '\nAntal: ' +str(self.get_antal())+  \
                 ' \nPris: ' +str(self.get_pris())#Typar om antal och pris till sträng.
        return utskrift
