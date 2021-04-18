import MYexample as kortlek

class Spelare():
    def __init__(self, leken, namn = 'Spelaren'):
        self._lek = leken
        self._namn = namn
        self._hand = []
        self._poäng = 0
        self._antal_ess = 0

    def nytt_kort(self):
        k = self._lek.give()
        self._hand.append(k)
        if k.get_value() == 1:
            self._poäng += 14
            self._antal_ess += 1
        else:
            self._poäng += k.get_value()
        if self._poäng > 21 and self._antal_ess > 0:
            self._poäng -= 13
            self._antal_ess -= 1

    def korten(self):
        return ', '.join([str(k) for k in self._hand])

    def utskrift(self):
        print(self._namn, 'have:', self.korten(),
              'and', self._poäng, 'points')

class Användare(Spelare):
    def spela(self):
        while True:
            self.nytt_kort()
            self.utskrift()
            if self._poäng > 21 \
               or not fortsätta('One more card. y/n'):
                break
        return self._poäng


class Dator(Spelare):
    def spela(self):
        while self._poäng <= 16:
            self.nytt_kort()
        self.utskrift()
        return self._poäng

def fortsätta(fråga):
    s = input(fråga + '? ')
    return len(s) > 0 and (s[0] == 'y' or s[0] == 'Y')

print('Welcome to blackjack')
while True:
    lek = kortlek.Cardgame()
    du = Användare(lek, 'You')
    datorn = Dator(lek, 'Computer')
    p1 = du.spela()
    if p1 > 21:
        print('You loose')
    elif p1 == 21:
        print('You win')
    else:
        p2 = datorn.spela()
        if p2 <= 21 and p2 >= p1:
            print('You loose')
        else:
            print('You win')
    if not fortsätta('New round y/n'):
        break