import random #Importerar slumpgenerator random.
#Variabler.
stickor = 21 #Totalt 21st stickor från början.
spel = True #Variabel för att bestämma när while loopen startar.

print(f"Det finns {stickor} stickor att spela med") #Skriver ut antal stickor att spela med.

while spel: #While loop för att kunna starta spelet.Om spel = True startar loopen.
    
    drag = int(input("Hur många stickor vill du ta? En eller två?")) #Variabel som tilldelas en input med värdet av en integer.
   #Villkor för att avrunda om användaren skriver in för hög siffra.
    if drag > 2: 
        drag = 2 
        print("Du valde ett för högt nummer, det avrundas till två")#Utskrift.
    #Villkor för att avrunda om användaren skriver in för låg siffra.
    elif drag < 1:
        drag = 1
        print("Du valde ett för lågt nummer, det avrundas till ett")#Utskrift.
    stickor = stickor - drag #Variabeln stickor får ett nytt värde med uträkningen stickor - drag.
   
    #Om stickorna är slut för användaren, avslutas spelet(loopen) då spel tilldelas värdet False.
    if stickor <= 0:
      spel = False 
      print("Det var sista stickan, användaren förlorade!")#Utskrift. 
      break #Break bryter loopen, så att datorn(slumpgenerator) inte drar en sista gång.
    print(f"Det finns {stickor} stickor kvar")#Skriver ut hur hur många stickor finns kvar.
    #Om stickor är större än 2, slumpar datorn ett värde mellan 1 och 2.
    if stickor > 2:
        dator = random.randint(1,2) #Variabel dator tilldelas värde 1 eller 2 genom slumpgenerator.
    else:#Annars om stickor är 2 eller mindre får datorn bara ta 1 sticka.
        dator = 1
    print(f"Datorn tog {dator}")#Utskrift

    stickor = stickor - dator #Stickor får ett nytt värde efter datorn har dragit stickor.
    print(f"Det finns {stickor} stickor kvar")#Utskrift
    #Om stickorna är slut för datorn , avslutas spelet(loopen) då spel tilldelas värdet False.
    if stickor <= 0:
        spel = False
        print("Det var sista stickan, datorn förlorade!")


        
        
    
    
    



    


