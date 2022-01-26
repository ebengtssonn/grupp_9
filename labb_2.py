#Input från användaren.
#Bränsletankens storlek. Datatyp integer.
bransleTank = int(input("Hur stor är bilens bränsletank? ange i hela liter:"))

#Sträcka per tank. Datatyp integer.
stracka = int(input("Hur långt kan du åka på en tank? ange i hela mil:"))

#Räknar ut förbrukningen genom att dividera liter med mil.
#Här blir förbrukningen av datatypen integer.
forbrukning = bransleTank / stracka

#Skriver ut bilens förbrukning och anger om det är en miljöbil eller inte med hjälp av boolean.
print(f" Din bil drar {forbrukning} liter per mil. Klassas den som miljöbil: ", bool(forbrukning <=0.5))
#Typar om förbrukningen till boolean.

