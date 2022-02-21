import shoppinglista_funktioner #importerar filen "shoppinglista_funktioner" med alla funktioner. 

def main(): #Definierar funktionen main()
    shoppinglista = ['mjölk', 'ägg'] #variabeln shoppinglista innehåller listan med värden (varorna). 

    while True: #while loop för att kunna köra programmet så länge som True gäller.
        print('\n''Välkommen till menyn för shoppinglistan! Välj ett alternativ ur menyn:') #startfras.
        #Variabel för att kunna ta emot ett manyval av användaren i form av en integer. 
        menyVal = int(input( '1 för att lägga till,' '\n' '2 för att skriva ut,' '\n' '3 för att ta bort,' 
        '\n' '4 för att ta bort en specifik punkt på listan' '\n' '5 för att se antal i listan,' 
        '\n' '6 för att läsa en punkt på listan,' '\n' '7 för att avsluta shoppinglistan.' '\n' 'Vilket alternativ väljer du?:'))
        #Villkor för att kolla vilket menyval som ska köras. 
        if menyVal == 1: #Anropar funktionen för att lägga till vara.
            shoppinglista_funktioner.adderaVara(shoppinglista)
        if menyVal == 2: #Anropar funktionen för att skriva ut varor på listan.
            shoppinglista_funktioner.utskriftVaror(shoppinglista)
        if menyVal == 3: #Anropar funktionen för att ta bort en vara på listan.
            shoppinglista_funktioner.taBortVara(shoppinglista)
        if menyVal == 4: #Anropar funktionen för att ta bort en vara baserat på indexposition.
            shoppinglista_funktioner.taBortIndex(shoppinglista)
        if menyVal == 5: #Anropar funktionen för att se antal varor på listan.
            shoppinglista_funktioner.antalVaror(shoppinglista)
        if menyVal == 6: #Anropar funktionen för att skriva ut vara på specifik indexposition.
            shoppinglista_funktioner.skrivUtIndex(shoppinglista)
        if menyVal == 7: #Avslutar programmet shoppinglistan.
            print('Nu avslutas shoppinglistan!') #Avslutande utskrift.
            break #break för att avsluta loopen. 
main() #anropar för att köra funktionen main()
        
