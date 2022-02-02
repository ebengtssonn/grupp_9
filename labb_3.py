import random
stickor = 21 #Totalt 21st stickor från början.
run = True

print(f"Det finns {stickor} stickor att spela med")

while run:
    
    #print(f"Det finns {stickor} stickor kvar")
    drag = int(input("Hur många stickor vill du ta? En eller två?"))
   
    if drag > 2:
        drag = 2
        print("Du valde ett för högt nummer, det avrundas till två")
    
    elif drag < 1:
        drag = 1
        print("Du valde ett för lågt nummer, det avrundas till ett")
    stickor = stickor - drag
   

    if stickor <= 0:
      run = False 
      print("Det var sista stickan, användaren förlorade!")
      break
    print(f"Det finns {stickor} stickor kvar")

    if stickor > 2:
        dator = random.randint(1,2)
    else:
        dator = 1
    print(f"Datorn tog {dator}")

    stickor = stickor - dator
    print(f"Det finns {stickor} stickor kvar")

    if stickor <= 0:
        run = False
        print("Det var sista stickan, datorn förlorade!")


        
        
    
    
    



    


