import random #importerar slumpgenerator random
#variabler
studenter = 145
#tilldelas värdet 0 innan vi börjar räkna
mvg = 0
vg = 0
g = 0
u = 0
totResultat = 0
#skapar en textfil för att kunna skriva in betyg.
wFil = open('resultat.txt', 'w')
for i in range(145): #en loop för att skriva in 145st resultat
    betyg = random.randint(45,100) #slumpar ett värde(heltal)till betyg mellan 45 och 100
    wFil.write(str(betyg)+'\n') #skriver in det slumpade talet i textfilen
wFil.close() # stänger textfilen

rFil = open('resultat.txt', 'r')#För att öpnna filen och för att kunna läsa den.

for resultat in rFil: #forloop för att kunna kontrollera alla rader i läsfilen.
    #villkor för att kontrollera vilken betygskategori resultatet hamnar i
    #samt håller räkningen för just det betyget
    if int(resultat) >= 90: #typar om från string till int
        mvg += 1 
    elif int(resultat) >= 76:
        vg += 1
    elif int(resultat) >= 60:
        g += 1
    else: #om inget av ovan nämnda gäller blir betyget ett U
        u += 1
    totResultat += int(resultat) #ny variabel för att kunna lgga ihop det totala resultatet. Resultatet typas om till int
rFil.close() #Stänger läsfilen.
medelvarde = totResultat / studenter #Räknar ut medelvärde.
#Skriver ut resultatet
print('Resultatet för tentan är:') 
print(f'{mvg} stycken MVG, {vg} stycken VG, {g} stycken G och {u} stycken U.' )#skriver ut antal av varje betyg.
antal = mvg + vg + g #Räknar ut antal studenter som fick 60 poäng och över.
print(f'Det var totalt {antal} stycken studenter som fick 60 poäng och över.')#skriver ut antal som fick 60 och över.
andel = float((mvg + vg + g)/studenter) #räknar ut hur många procent som fick 60 och över.
print(f'I procent blir det {andel*100:.1f}% av studenterna som fick 60 poäng och över.') #skriver ut resultatet i %.
print(f'Medelvärdet av alla resultat blir {medelvarde:.1f} poäng.')#Skriver ut medelvärdet.
