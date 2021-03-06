#Funktion för menyval 1
def adderaVara(listan): #Definierar funktionen
    vara = input('\n''Vilken vara vill du lägga till i shoppinglistan?') #Variabel för att kunna ta emot en vara att addera. 
    listan.append(vara) #Funktion som lägger till den inmatade varan till listan
    print(f'Du har lagt till {vara} i shoppinglistan.') #utskrift

#Funktion för menyval 2
def utskriftVaror(listan): #Definierar funktionen
    print('Varor i shoppinglistan:') #utskrift
    for vara in listan: #for loop för att skriva ut varorna på ett snyggare sätt.
        print(f'{vara},',  end = ' ')
    print('')#Vi ville ha en blankrad

#Funktion för menyval 3
def taBortVara(listan): #Definierar funktionen
    vara = input('Vilken vara vill du ta bort?') #Variabel för att ta emot vilken vara som ska tas bort.
    listan.remove(vara) #funktionen som tar bort den valda varan från listan. 
    print(f'Du tog bort {vara} från shoppinglistan.') #utskrift

#Funktion för menyval 4
def taBortIndex(listan): #Definierar funktionen
    #Variabel som tilldelas funktionen pop med en input för att kunna radera en punkt efter indexvärde. 
    index = listan.pop(int(input('Vilken punkt i shoppinglistan vill du ta bort?'))) 
    print(f'Du tog bort {index} från shoppinglistan.') #utskrift

#Funktion för menyval 5
def antalVaror(listan): #Definierar funktionen
    antalVaror = len(listan) #anropar funktionen len som returnerar värdet
    print(f'Antal varor i shoppinglistan: {antalVaror}') #utskrift

#Funktion för menyval 6
def skrivUtIndex(listan): #Definierar funktionen 
    #Variabel som tilldelas en input (int) från användaren för att läsa specifik punkt på listan efter indexvärde.
    index = int(input('Vilken punkt i shoppinglistan vill du se?')) 
    print(listan[index]) #utskrift
