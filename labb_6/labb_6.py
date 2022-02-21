import shoppinglista_funktioner #importerar filen "shoppinglista_funktioner" med alla funktioner. 
import shopping

def main(): #Definierar funktionen main()
    again = True #Tilldelar again värdet true för att kunna köra loopen

    vara1 = shopping.Shopping('mjölk',5,15)
    vara2 = shopping.Shopping('ägg',12,10)
    vara3 = shopping.Shopping('bröd',20,20)

    shoppinglista = [vara1, vara2, vara3] #variabeln shoppinglista innehåller listan med objekten(varorna).


    while again: #while loop för att kunna köra programmet så länge som True gäller.
        print('\n''Välkommen till menyn för shoppinglistan! Välj ett alternativ ur menyn:') #startfras.
        #Variabel för att kunna ta emot ett manyval av användaren i form av en integer. 
        menyVal = int(input( '1 - Lägg till vara,' '\n' '2 - Skriv ut antal varor på listan,' '\n' '3 - Info om en vara på listan,' 
        '\n' '4 - Skriv ut varor som finns på listan,' '\n' '5 - Info om alla varor på listan,' 
        '\n' '6 - Uppdatera antal och pris för vald vara,' '\n' '7 - Ta bort vara på listan,' '\n' '8 - Avsluta shoppinglistan.' '\n''Vilket alternativ väljer du?:'))
        #Villkor för att kolla vilket menyval som ska köras. 
        if menyVal == 1: #Anropar funktionen för att lägga till vara.
            shoppinglista_funktioner.adderaVara(shoppinglista)
        if menyVal == 2: #Anropar funktionen för att skriva ut varor på listan.
            shoppinglista_funktioner.antalVaror(shoppinglista)
        if menyVal == 3: #Anropar funktionen för att söka namn och skriva ut info om ett visst objekt på listan.
            shoppinglista_funktioner.skrivUtVara(shoppinglista)
        if menyVal == 4: #Anropar funktionen för att ta bort en vara baserat på indexposition.
            shoppinglista_funktioner.taBortIndex(shoppinglista)
        if menyVal == 5: #Anropar funktionen för att se antal varor på listan.
            shoppinglista_funktioner.utskriftVaror(shoppinglista)
        if menyVal == 6: #Anropar funktionen för att skriva ut vara på specifik indexposition.
            
            shoppinglista_funktioner.taBortVara(shoppinglista)
        if menyVal == 7: #Avslutar programmet shoppinglistan.
            print('Nu avslutas shoppinglistan!') #Avslutande utskrift.
            break #break för att avsluta loopen. 
main() #anropar för att köra funktionen main()