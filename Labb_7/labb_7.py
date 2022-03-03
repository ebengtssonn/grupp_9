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
    t_area.insert(END, len(shopping_dict))#skriver ut en specifik plats

#Funktion 3
def info_func():
    t_area.delete('1.0', END) #rensar innan 
    sokt_vara = e_info.get()
    for v in shopping_dict.values():
        if sokt_vara.lower() in v.getNamn().lower():
            t_area.insert(END, v)

#Funktion 4
def namn_func():
    t_area.delete('1.0', END) #rensar innan 
    for v in shopping_dict.values():
        t_area.insert (END,f'{v.getNamn()} \n')

#Funktion 5
def helaListan_func():
    t_area.delete('1.0', END) #rensar innan 
    for v in shopping_dict.values():
        t_area.insert (END,f' {v} \n')
        t_area.insert (END,'---------------\n')

#funktion 6 
def uppdatera_func():
    t_area.delete('1.0', END) #rensar innan

root = Tk()#instans av klassen
root.title('Shopping')

lbl_namn = Label(root, text = 'Fyll i vara:')#namn lbl, klass Label , Text ='' detsamma som print
lbl_namn.grid(row = 0, column = 0)
lbl_antal = Label(root, text = 'Fyll i antal:')#namn lbl, klass Label , Text ='' detsamma som print
lbl_antal.grid(row = 1, column = 0)
lbl_pris = Label(root, text = 'Fyll i pris:')#namn lbl, klass Label , Text ='' detsamma som print
lbl_pris.grid(row = 2, column = 0)
lbl_info = Label(root, text = 'Sök namn på vara:')
lbl_info.grid(row = 3, column = 0)

e_namn = Entry(root, width=40, borderwidth=5)#klassen entry har skapats med objektet e_namn
e_namn.grid(row=0, column=1)
e_antal = Entry(root, width=40, borderwidth=5)#klassen entry har skapats med objektet e_namn
e_antal.grid(row=1, column=1)
e_pris = Entry(root, width=40, borderwidth=5)#klassen entry har skapats med objektet e_namn
e_pris.grid(row=2, column=1)
e_info = Entry(root, width=40, borderwidth=5)#klassen entry har skapats med objektet e_namn
e_info.grid(row=3, column=1)



btn_addera = Button(root, text='Lägg till', padx=30, pady=20, command=addera_func)
btn_addera.grid(row=4, column=0)
btn_antal = Button(root, text='Antal varor', padx=30, pady=20, command=antal_func)
btn_antal.grid(row=4, column=1)
btn_sok = Button(root, text='Visa info (sök på namn)', padx=30, pady=20, command=info_func)
btn_sok.grid(row=4, column=2)
btn_namn = Button(root, text='Visa namn på alla varor)', padx=30, pady=20, command=namn_func)
btn_namn.grid(row=4, column=3)
btn_helaListan = Button(root, text='Visa hela listan', padx=30, pady=20, command=helaListan_func)
btn_helaListan.grid(row=4, column=4)

t_area = Text(root, height=100, width=60)
t_area.grid(row=5, column=0, columnspan=3)



root.mainloop()#objektet root anropas
