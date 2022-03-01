import shoppinglista_funktioner #Importerar filen "shoppinglista_funktioner" med alla funktioner. 
import shopping #Importerar klassfilen.

def main(): #Definierar funktionen main().
    igen = True #Tilldelar igen värdet true för att kunna köra loopen.
    #Variabler som tilldelas värden för varje vara (namn, antal, pris).
    vara1 = shopping.Shopping('mjölk',5,15)
    vara2 = shopping.Shopping('ägg',12,10)
    vara3 = shopping.Shopping('bröd',20,20)

    shoppinglista = [vara1, vara2, vara3] #Variabeln shoppinglista innehåller listan med objekten(varorna).

    while igen: #While loop för att kunna köra programmet så länge som igen är True.
        print('\n''Välkommen till menyn för shoppinglistan! Välj ett alternativ ur menyn:') #Startfras.
        #Variabel för att kunna ta emot ett menyval av användaren i form av en integer. 
        menyVal = int(input( '1 - Lägg till vara,' '\n' '2 - Skriv ut antal varor på listan,' '\n' '3 - Info om en vara på listan,' 
        '\n' '4 - Skriv ut varor som finns på listan,' '\n' '5 - Info om alla varor på listan,' 
        '\n' '6 - Uppdatera antal och pris för vald vara,' '\n' '7 - Ta bort vara på listan,' '\n' '8 - Avsluta shoppinglistan.' '\n''Vilket alternativ väljer du?'))
        #Villkor för att kolla vilket menyval som ska köras. 
        if menyVal == 1: #Anropar funktionen för att lägga till vara.
            shoppinglista_funktioner.adderaVara(shoppinglista)
        if menyVal == 2: #Anropar funktionen för att skriva ut antal varor på listan.
            shoppinglista_funktioner.antalVaror(shoppinglista)
        if menyVal == 3: #Anropar funktionen för skriva ut info om en vara på listan.
            shoppinglista_funktioner.skrivUtVara(shoppinglista)
        if menyVal == 4: #Anropar funktionen för att skriva ut vilka varor som finns på listan.
            shoppinglista_funktioner.skrivUtNamn(shoppinglista)
        if menyVal == 5: #Anropar funktionen för att skriva ut info om alla varor på listan.
            print('Alla varor i listan:')
            shoppinglista_funktioner.skrivUtAlla(shoppinglista)
        if menyVal == 6: #Anropar funktionen för att uppdatera antal och pris för en vara.
            shoppinglista_funktioner.uppdateraVara(shoppinglista)
        if menyVal == 7: #Tar bort vara från listan.
            #Menyval för att kunna välja att ta bort indexposition eller namn på vara.
            val = int(input('Välj 1 för att ange indexpositionen för den varan du vill ta bort, \nVälj 2 för att ange namnet på varan du vill ta bort:'))
            if val == 1:#Om val är lika med 1 så blir index vald.
                shoppinglista_funktioner.taBortIndex(shoppinglista)
            if val == 2:#Om val är lika med 2 så blir namn vald.
                shoppinglista_funktioner.taBortNamn(shoppinglista)
        if menyVal == 8: #Avslutar programmet shoppinglistan.
            print('Nu avslutas shoppinglistan!') #Avslutande utskrift.
            igen = False #igen tilldelas false för att avsluta loopen. 

main() #anropar för att köra funktionen main()