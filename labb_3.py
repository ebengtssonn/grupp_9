import random
stickor = 21 #Totalt 21st stickor från början.
run = True

while run:
    if stickor > 0:
        print(f"Det finns {stickor} stickor kvar")
    

    drag1 = int(input("Hur många stickor vill du ta? En eller två?"))
   

    if drag1 > 2:
        drag1 = 2
    
    elif drag1 < 1:
        drag1 = 1
    stickor = stickor - (drag1)
    

    if stickor <= 0:
      run = False 
      print("Det var sista stickan, användaren förlorade!")
      break
    if stickor > 2:
        dator = random.randint(1,2)
    else:
        dator = 1
        print(f"Datorn tog {dator}")

stickor = stickor - (dator)
print(f"Det finns {stickor} stickor kvar")

if stickor <= 0:
        run = False 
        print("Det var sista stickan, användaren förlorade!")
        
    
    
    



    


