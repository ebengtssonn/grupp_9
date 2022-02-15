def adderaVara(listan):#definerat lista
    vara = input('Vilken vara vill du lägga till?')
    listan.append(vara)

def taBortVara(listan):
    vara = input('Vilken vara vill du ta bort?')
    listan.remove(vara)

def antalVaror(listan):
    antalVaror = len(shoppinglista)#anropar funktionen len som returnerar värdet
    print(f'Antal varor på listan: {antalVaror}')