import random
class Card:
    def __init__(self, val, suit, faceup=True):
        self.val=val
        self.suit=suit
        self.faceup=faceup

    def show(self):
        if self.faceup:
            print(str(self.val) + " of " + self.suit)
        else:
            print("Card is face down")

class Deck:
    def __init__(self):
        self.cards=[]
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(v,s, False))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r=random.randint(0,i)
            self.cards[i], self.cards[r]=self.cards[r], self.cards[i]
deck=Deck()
deck.shuffle()
class Hand:
    def __init__(self):
        self.cards=[]

    def show(self):
        for card in self.cards:
            card.show()

    def draw(self, faceup=True, deck=deck):
        card=deck.cards[0]
        if not faceup:
            card.faceup=False
        else:
            card.faceup=True
        self.cards.append(card)
        deck.cards.remove(card)

class Player:
    def __init__(self):
        self.hand=Hand()
        self.frontdown=Hand()
        self.frontup=Hand()
        for i in range(3):
            self.hand.draw()
            self.frontup.draw()
            self.frontdown.draw(faceup=False)


    def show(self):
        print("Hand:")
        for card in self.hand.cards:
            card.show()
        print("In front:")
        for card in self.frontup.cards:
            card.show()
        for card in self.frontdown.cards:
            card.show()

playpile=Hand()
def Play(card):
    if card.val==10:#Lets 10 be played any time
        playpile=Hand()#Lets 10 remove all cards in the pile from play
    elif card.val==1 or card.val==2:#Lets ace and 2 be played any time
        playpile.append(card)
    elif card.val > playpile[-1].val:#Checks if the card is greater then the current top of the pile
        playpile.append(card)

players={}
pcount=input("How many players? ")
if int(pcount)>5:
    print("Too many players")
else:
    for p in range(int(pcount)):
        players[p]=Player()
