 # = TILLDELNING
 # == jämförelse

# KODBLOCK = ett antal rader som hör ihop
# Om age == 50 OCH heter Stefan
# 
#amn = input("Vad heter du?")
# age = int(input("Hur gammal är du"))
# if age == 13:
#     print("Du har precis blivit tonåring")
#     print("Fasen vad kul")
# elif age == 50 and ( namn == "Stefan" or namn == "Kalle" ):
#     print("Du är ung ändå")
#     print("Ingen fara")
# elif age >= 67:
#     print("Är du pensionär?")
#     print("Skönt att slippa jobba")
# else:
#     print("Ja men det är ju en bra ålder")
#     print("Det också")
# print("Slut")
# () kommer vi använda föär att KÖRA EN FUNKTION 
# [] bara för att komma åt enskilda delar i en lista (sekvens of chars)
# {} i Python endast används i f-string 
# age = 12
# namn = "Stefan"
# print("Age:"  + str(age) + " namn:" + namn)
# b = 3.14
#print(f"Age:{age} namnä:{namn} och {b} vetdu 12 + 12 är {12+12} japp  ")



print("1. Skapa ny maträtt")
print("2. Lista alla")
print("3. Ändra maträtt")
print("4. Lista dagens meny")
print("0. Avsluta")
selection = input("Ange val:")
if selection == "1":
    dish = input("Ange maträttes namn")
    dish = dish.strip()
    print(f"Längden är {len(dish)}")
elif selection == "2":
    print("Lista alla")
elif selection == "3":
    print("Ändra maträtt")
elif selection == "4":
    print("Lista dagens meny")
elif selection == "0":
    print("Avsluta")




