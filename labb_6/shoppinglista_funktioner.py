import shopping#Importerar klassfilen shopping.

#Funktion för menyval 1.
def adderaVara(listan): #Definierar funktionen.
    #Variabler för info om ny vara.
    namn = input('Namn på vara:')
    antal = int(input('Antal av vara:'))
    pris = int(input('Pris på vara:'))
    vara = shopping.Shopping(namn, antal, pris) #Variabel för att kunna ta emot en vara att addera. 
    listan.append(vara) #Funktion som lägger till den inmatade varan till listan.
    print(f'Du har nu lagt till {namn} i shoppinglistan.') #Utskrift.

#Funktion för menyval 2
def antalVaror(listan): #Definierar funktionen.
    antalVaror = len(listan) #Anropar funktionen len som returnerar antal objekt i listan.
    print(f'Antal varor i shoppinglistan: {antalVaror}') #Utskrift.

#Funktion för menyval 3
def skrivUtVara(listan): #Definierar funktionen.
    #Variabel som tilldelas en input från användaren för att läsa info om en specifik vara från listan.
    vilkenVara = input('Vilken vara i shoppinglistan vill du ha info om?')
  #Forloop för att kolla namnet på varan om den finns med på listan.
    for i in listan:
        #Om namnet stämmer överens med namnet på listan så printas varans info.
        if vilkenVara == i.getNamn():
            print(i)
            break
    
#Funktion för menyval 4
def skrivUtNamn(listan): #Definierar funktionen.
    #Forloop för att skriva ut namnet på alla varor som finns på listan.
    for i in listan:
        print(i.getNamn())

#Funktion för menyval 5
def skrivUtAlla(listan): #Definierar funktionen.
    #Forloop för att skriva ut info om alla varor som finns på listan.
    for i in listan:
        print(i)
        print()# Blankrad mellan varor.

#Funktion för menyval 6
def uppdateraVara(listan): #Definierar funktionen.
    vara = input('Vilken vara vill du uppdatera?') #Variabel för att välja vilken vara som ska uppdateras.
    #Variabler för ny info. Användaren anger antal och pris.
    nyttAntal = int(input('Ange nytt antal: '))
    nyttPris = int(input('Ange nytt pris: '))
    #Forloop för att gå igenom listan.
    for i in listan:
        #Om namnet finns med på listan uppdateras antal och pris för den varan.
        if vara == i.getNamn():
           i.setAntal(nyttAntal)
           i.setPris(nyttPris)
           print('-------------------------')
           print(f'Det nya antalet är: {i.getAntal()} \nDet nya priset är: {i.getPris()} ')

#Funktion för menyval 7.1
#Definerar funktion för att ta bort vald indexposition.
def taBortIndex(listan):
        index = int(input('Vilken indexposition i listan vill du ta bort?'))#Variabel för att ta emot input från användaren.
        del listan[index]#Del används för att ta bort indexposition på listan.
        print(f'Du tog bort punkt nr.{index} från listan')

#Funktion för menyval 7.2
def taBortNamn(listan):
        vara = input('Vilken vara vill du ta bort från listan?')#Variabel för att ta emot input från användaren.
        #Forloop för att hitta rätt namn i listan.
        for i in listan:
            if vara == i.getNamn():
                listan.remove(i)#Remove används för att ta bort vara på listan.
                print(f'Du tog bort {vara} från shoppinglistan.')
