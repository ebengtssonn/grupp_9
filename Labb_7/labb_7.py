from tkinter import *
import shopping
import funktioner


vara1 = shopping.Shopping('mjölk',5,15)
vara2 = shopping.Shopping('ägg',12,10)
vara3 = shopping.Shopping('bröd',20,20)

shopping_dict = {1 : vara1, 2 : vara2, 3 : vara3} #Variabeln shoppinglista innehåller listan med objekten(varorna).


id=3
#Funktion 1
def addera_func():#add funktion
    global id
    id += 1 # id = id+1
    namn = e_namn.get()
    antal = int(e_antal.get())
    pris = int(e_pris.get())
    #print(namn, antal,pris)#skriver ut för att testa i terminal
    vara = shopping.Shopping(namn, antal, pris)
    shopping_dict[id] = vara
    print(shopping_dict[id])
    t_area.insert(END, shopping_dict[id])#skriver ut en specifik plats

#Funktion 2
def antal_func():#add funktion
    
    #print(len(shopping_dict))
    t_area.insert(END, len(shopping_dict))#skriver ut en specifik plats

root = Tk()#instans av klassen
root.title('Shopping')

lbl_namn = Label(root, text = 'Fyll i vara:')#namn lbl, klass Label , Text ='' detsamma som print
lbl_namn.grid(row = 0, column = 0)
lbl_antal = Label(root, text = 'Fyll i antal:')#namn lbl, klass Label , Text ='' detsamma som print
lbl_antal.grid(row = 1, column = 0)
lbl_pris = Label(root, text = 'Fyll i pris:')#namn lbl, klass Label , Text ='' detsamma som print
lbl_pris.grid(row = 2, column = 0)

e_namn = Entry(root, width=40, borderwidth=5)#klassen entry har skapats med objektet e_namn
e_namn.grid(row=0, column=1)

e_antal = Entry(root, width=40, borderwidth=5)#klassen entry har skapats med objektet e_namn
e_antal.grid(row=1, column=1)
e_pris = Entry(root, width=40, borderwidth=5)#klassen entry har skapats med objektet e_namn
e_pris.grid(row=2, column=1)

btn_addera = Button(root, text='Lägg till', padx=30, pady=20, command=addera_func)
btn_addera.grid(row=3, column=0)

btn_antal = Button(root, text='Antal varor', padx=30, pady=20, command=antal_func)
btn_antal.grid(row=3, column=1)

t_area = Text(root, height=100, width=60)
t_area.grid(row=4, column=0, columnspan=3)



root.mainloop()#objektet root anropas
