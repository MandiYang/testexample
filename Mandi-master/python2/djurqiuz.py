def kontrollera_gissning(gissning, svar):
    global poäng
    if gissning.lower() == svar.lower():
        print('Rätt svar')
        poäng = poäng + 1
poäng = 0
print('Gissa djuret!')
gissning1 = input('Vilket djur har 4ben och har lång hals? ')
kontrollera_gissning(gissning1, 'giraff')
gissning2 = input('Vilket är den långsamaste landdjuret? ')
kontrollera_gissning(gissning2, 'sköldpadda')
gissning3 = input('Vilket är den giftigaste organism? ')
kontrollera_gissning(gissning3, 'pilgiftgroda')

print('Din poäng är ' + str(poäng))
        
