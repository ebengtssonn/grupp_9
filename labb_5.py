import shoppinglista_funktioner
def main():
    shoppinglista = ['mjölk', 'ägg']

    while True:
        menyVal = int(input('Välj 1 för att lägga till, \
        2 för att skriva ut, 3 ta bort, 4 se antal i listan \
            5 avsluta'))
        if menyVal == 1:
            shoppinglista_funktioner.adderaVara(shoppinglista)#Anropar funktionen add_vara för att lägga till vara.
        if menyVal == 2:
            print(shoppinglista) #kan även lopa igenom glasslista för utskrift
        if menyVal == 3:
            shoppinglista_funktioner.taBortVara(shoppinglista)
        if menyVal == 4:
            
        if menyVal == 5:
            print('Nu avslutas programmet')
            break
main()
        
