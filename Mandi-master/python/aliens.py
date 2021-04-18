aliens = 2
password = "BASTU4"
print('Skynda dig! Utomjordingarna  är på väg!')
print('Du måste aktivera det globala försvarssystemet.')
print('Hoppa verkligen du kan lösenordet.')
print()
print('-------------------------------------------------')
print('      VÄLKOMMEN TILL DET GLOBALA FÖRSVARSSYSTEMET')
print('-------------------------------------------------')
print()
gissa = input('Var vänligen att skriva lösenordet: ').upper()
while gissa != password:
    print()
    print('Fel lösenord.')
    print()
    aliens = aliens ** 2
    print('Det finns', aliens, 'utomjordingar nu. Försök igen!')

    if aliens > 7410000000:
        break
    print()
    print('Tips: alla hus i Finland har det nästan \
    och en siffra.')
    print()
    gissa = input('Var vänligen att snabbt skriva lösenordet nu: ').upper()
if aliens > 7410000000:
    print('Neeeeeej! Utomjordingarna tar över. Allt är förlorat!')
else:
    print('Hurra! Vi vann striden. Tack! Jorden är räddad!')
