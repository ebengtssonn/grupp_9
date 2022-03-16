from tkinter import * #importerar tkinter
import class_shopping # importerar klassenfilen shopping
 
#variabler med varor som finns med shoppinglistan från början
vara1 = class_shopping.Shopping('mjölk',5,15)
vara2 = class_shopping.Shopping('ägg',12,10)
vara3 = class_shopping.Shopping('bröd',20,20)

shopping_dict = {1 : vara1, 2 : vara2, 3 : vara3} #Variabeln shoppinglista innehåller dict med objekten(varorna).


id=3 #anger start id
#Funktion 1
def addera_func():#add funktion
    t_area.delete('1.0', END) #rensar innan 
    global id #global variabel id
    id += 1 # id = id+1 för att kunna lägga till vara
    namn = e_namn.get() #variabel för att kunna ta emot angivet namn
    antal = int(e_antal.get()) # variabel för att kunna ta emot angivet antal, typar om till int
    pris = int(e_pris.get()) #variabel för att kunna ta emot pris, typar om till int
    vara = class_shopping.Shopping(namn, antal, pris) # varaibel för att hämta objektet vara från klassfilen
    shopping_dict[id] = vara # varan tilldelas sitt id i dict
    t_area.insert(END,'Du har lagt till varan: \n') #skriver ut
    t_area.insert(END, shopping_dict[id])#skriver ut 
    antal_lbl = Label(root, text='Det finns '+str(len(shopping_dict))+'varor i shoppinglistan')#textlabel för att visa aktuellt antal i shoppinglistan
    antal_lbl.grid(row=3,column=2)

#Funktion 2
def antal_func():#funktion för antal varor
    t_area.delete('1.0', END) #rensar innan 
    t_area.insert(END, len(shopping_dict))#skriver ut antal varor i dict med hjälp av len

#Funktion 3
def info_func(): #funktion för att hämta info om vald vara
    t_area.delete('1.0', END) #rensar innan 
    sokt_vara = e_namn.get() #variabel för att ta emot det sökta namnet
    for v in shopping_dict.values(): #Loop för att hitta objektet med rätt namn/ värde
        if sokt_vara.lower() in v.get_namn().lower(): #kan läsa av både versaler och gemener
            t_area.insert(END, v)# skriver ut

#Funktion 4
def namn_func(): #funktion för att skriva ut alla namn
    t_area.delete('1.0', END) #rensar innan 
    for v in shopping_dict.values(): #loopar igenom dict
        t_area.insert (END,f'{v.get_namn()} \n')#skriver ut namnet för varje varv

#Funktion 5
def hela_listan_func():# funktion för att skriva ut all info om alla varor i listan
    t_area.delete('1.0', END) #rensar innan 
    for v in shopping_dict.values(): #loopar igenom dict
        t_area.insert (END,f' {v} \n') #skriver ut infon om varje vara
        t_area.insert (END,'---------------\n')

#funktion 6 
def uppdatera_func(): #funktion för att uppdatera pris och antal
    t_area.delete('1.0', END) #rensar innan
    nytt_pris = int(e_pris.get()) #variabel för att kunna ta emot nytt pris
    nytt_antal = int(e_antal.get()) #variabel för att kunna ta emot nytt antal
    vara = e_namn.get() #varabel för att ta emot vilken vara som ska ändras
    for i in shopping_dict.values(): #For-loop för att gå igenom dict och hitta rätt item
        if vara == i.get_namn(): #kollar så namnet i dict stämmer med det inmatade
            i.set_antal(nytt_antal) #sätter nytt antal
            i.set_pris(nytt_pris) #sätter nytt pris
            break #stoppar loopen
    t_area.insert (END,'Nu är varan uppdaterad: \n') #utskrift
    t_area.insert (END, i)#utskrift av uppdaterad vara

#funktion 7
def ta_bort_func(): #funktion för att ta bort valt id
    t_area.delete('1.0', END) #rensar innan 
    id = int(e_id.get()) #variabel för att ta emot valt id. Typar om till int
    del shopping_dict[id] #använder funktionen del för att ta bort valt id från dictionaryn. 
    t_area.insert (END, f'Du tog bort nr: {id}') #skriver ut vilket id som togs bort.
    antal_lbl = Label(root, text='Det finns '+str(len(shopping_dict))+'varor i shoppinglistan')#textlabel för att visa aktuellt antal i shoppinglistan
    antal_lbl.grid(row=3,column=2)
   
#GUI
root = Tk()
root.title('Shopping')


lbl_namn = Label(root, text = 'Fyll i namn på vara:') #deklarerar textlabel
lbl_namn.grid(row = 0, column = 0) #placerar ut/ lägger in textlabel på gui
lbl_antal = Label(root, text = 'Fyll i antal:')
lbl_antal.grid(row = 1, column = 0)
lbl_pris = Label(root, text = 'Fyll i pris:')
lbl_pris.grid(row = 2, column = 0)
lbl_id = Label(root, text = 'Ange ID för att ta bort vara:')
lbl_id.grid(row = 3, column = 0)
antal_lbl = Label(root, text='Det finns '+str(len(shopping_dict))+'varor i shoppinglistan')#textlabel för att visa aktuellt antal i shoppinglistan
antal_lbl.grid(row=3,column=2)

e_namn = Entry(root, width=40, borderwidth=5)#deklarerar/ skapar inputfält. Sätter bredd och ram.
e_namn.grid(row=0, column=1) #placerar ut inputfält i gui
e_antal = Entry(root, width=40, borderwidth=5)
e_antal.grid(row=1, column=1)
e_pris = Entry(root, width=40, borderwidth=5)
e_pris.grid(row=2, column=1)
e_id = Entry(root, width=40, borderwidth=5)
e_id.grid(row=3, column=1)

btn_addera = Button(root, text='Lägg till', padx=30, pady=20, command=addera_func) #deklarerar/ skapar upp knapp. Sätter padding och funktion som ska köras
btn_addera.grid(row=4, column=0, columnspan=1) #placerar ut knappen i gui. 
btn_sok = Button(root, text='Visa info (sök på namn)', padx=30, pady=20, command=info_func)
btn_sok.grid(row=4, column=2, columnspan=1)
btn_namn = Button(root, text='Visa namn på alla varor', padx=30, pady=20, command=namn_func)
btn_namn.grid(row=5, column=0, columnspan=1)
btn_hela_listan = Button(root, text='Visa hela listan', padx=30, pady=20, command=hela_listan_func)
btn_hela_listan.grid(row=5, column=1, columnspan=1)
btn_uppdatera = Button(root, text='Uppdatera (pris/antal)', padx=30, pady=20, command=uppdatera_func)
btn_uppdatera.grid(row=5, column=2, columnspan=1)
btn_ta_bort = Button(root, text='Ta bort  (ange ID)', padx=30, pady=20, command=ta_bort_func)
btn_ta_bort.grid(row=4, column=1, columnspan=1)

t_area = Text(root, height=100, width=100) #deklarerar/ skapar upp text area och bestämmer storlek. 
t_area.grid(row=6, column=0, columnspan=3) #placerar ut text area i gui. 
t_area.insert (END,'Välkommen till programmet för administartion av shoppinglistan!')




root.mainloop()#objektet root anropas
