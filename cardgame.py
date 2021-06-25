import random
class Card:
    def __init__(self, suit, val):
      self.suit=suit
      self.val=val

    def show(self):
        print(str(self.val) + " of " + self.suit)

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r=random.randint(0,i)
            self.cards[i], self.cards[r]=self.cards[r], self.cards[i]


deck=Deck()
deck.shuffle()
deck.show()
