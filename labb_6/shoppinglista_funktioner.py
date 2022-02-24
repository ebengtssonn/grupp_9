import shopping

#Funktion för menyval 1
def adderaVara(listan): #Definierar funktionen
    namn = input('Namn på vara:')
    antal = int(input('Antal av vara:'))
    pris = int(input('Pris på vara:'))
    vara = shopping.Shopping(namn, antal, pris) #Variabel för att kunna ta emot en vara att addera. 
    listan.append(vara) #Funktion som lägger till den inmatade varan till listan
    print(f'Du har nu lagt till {namn} i shoppinglistan.') #utskrift

#Funktion för menyval 2
def antalVaror(listan): #Definierar funktionen
    antalVaror = len(listan) #anropar funktionen len som returnerar värdet
    print(f'Antal varor i shoppinglistan: {antalVaror}') #utskrift

#Funktion för menyval 3
def skrivUtVara(listan): #Definierar funktionen 
    #Variabel som tilldelas en input (int) från användaren för att läsa specifik punkt på listan efter indexvärde.
    vilkenVara = input('Vilken vara i shoppinglistan vill du ha info om?')
    for i in listan:
        if vilkenVara == i.getNamn():
            print(i)
            break
    
#Funktion för menyval 4
def skrivUtNamn(listan): #Definierar funktionen
    for i in listan:
        print(i.getNamn())

    #Variabel som tilldelas funktionen pop med en input för att kunna radera en punkt efter indexvärde. 
    # index = listan.pop(int(input('Vilken punkt i shoppinglistan vill du ta bort?'))) 
    # print(f'Du tog bort {index} från shoppinglistan.') #utskrift

#Funktion för menyval 5
def skrivUtAlla(listan): #Definierar funktionen
    for i in listan:
        print(i)
        print()# blankrad mellan varor



#Funktion för menyval 6
def uppdateraVara(listan): #Definierar funktionen
    vara = input('Vilken vara vill du uppdatera?') #Variabel för att ta emot vilken vara som ska tas bort.
    nyttAntal = input('Ange nytt antal: ')
    nyttPris = input('Ange nytt pris: ')
    for i in listan:
        if vara == i.getNamn():
           i.setAntal(nyttAntal)
           i.setPris(nyttPris)
           print('-------------------------')
           print(f'Det nya antalet är: {i.getAntal()} \nDet nya priset är: {i.getPris()} ')


#Funktion för menyval 7.1
def taBortIndex(listan):
        index = int(input('Vilken indexposition i listan vill du ta bort?'))
        del listan[index]
        print(f'Du tog bort punkt nr.{index} från listan')

#Funktion för menyval 7.2
def taBortNamn(listan):
        vara = input('Vilken vara vill du ta bort från listan?')
        for i in listan:
            if vara == i.getNamn():
                listan.remove(i)
                print(f'Du tog bort {vara} från shoppinglistan.')
