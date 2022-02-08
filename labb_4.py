import random
#variabler
studenter = 145
#tilldelas värdet 0 innan vi börjar räkna
mvg = 0
vg = 0
g = 0
u = 0

#skapar en textfil för att kunna skriva in betyg.
w_file = open('resultat.txt', 'w')
for i in range(145): #en loop för att skriva in 145st resultat
    betyg = random.randint(45,100) #slumpar ett värde(heltal)till betyg mellan 45 och 100
    w_file.write(str(betyg)+'\n') #skriver in det slumpade talet i textfilen

#villkor för att kontrollera vilken batygskategori resultatet hamnar i
#samt håller räkningen för just det resultatet
    if betyg >= 90:
        mvg += 1 
    elif betyg >= 76:
        vg += 1
    elif betyg >= 60:
        g += 1
    else: #om inget av ovan nämnda gäller blir betyget ett U
        u += 1

print(f'Det finns {mvg} stycken MVG, {vg} stycken vg, {g} stycken g och {u} stycken u.' )#skriver ut antal av varje betyg  
w_file.close() # stänger textfilen

antal = mvg + vg + g
print(f'Det var totalt {antal} stycken studenter som fick 60 poäng och över.')#skriver ut antal som fick 60 och över

andel = float((mvg + vg + g)/studenter) #räknar ut hur många procent som fick 60 och över
print(f'I procent blir det {andel*100:.1f}% av studenterna som fick 60 poäng och över.') #skriver ut resultatet i %


