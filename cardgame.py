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
playpile=Hand()
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

def Play(card, originhand):
    if playcard.val==10:#Lets 10 remove all cards in the pile from play
        playpile.cards=[]
    else:
        playpile.cards.append(playcard)
    originhand.cards.remove(card)
    if deck.cards!=[] and len(originhand.cards)<4:
        originhand.draw()

players={}
pcount=input("How many players? ")
if int(pcount)>5:
    print("Too many players")
else:
    for p in range(int(pcount)):
        players[p]=Player()
gameover=False
while gameover==False:
    for p in players:
        print("Player "+str(p+1)+"'s turn")
        players[p].show()
        if playpile.cards==[]:
            print("The pile is currently empty")
        else:
            print("Current top of the pile: ")
            playpile.cards[-1].show()
        aplayablecard=False#Checks to see if the current player can play any cards
        for card in players[p].hand.cards:
            if card.val==10 or playpile.cards==[] or card.val==1 or card.val==2 or card.val >= playpile.cards[-1].val:
                aplayablecard=True
        if aplayablecard==False:
            input("No cards currently playable, drawing a card and skipping the turn...")
            if deck.cards!=[]:
                players[p].hand.draw()
        else:
            cardhasbeenplayed=False
            while cardhasbeenplayed==False:
                playcard=input("Which card would you like to play? ")
                playcard=int(playcard)-1
                playcard=players[p].hand.cards[playcard]
                if playcard.val==10 or playpile.cards==[] or playcard.val==1 or playcard.val==2 or playcard.val >= playpile.cards[-1].val:
                    Play(playcard, players[p].hand)
                    cardhasbeenplayed=True
                else:
                    print("You cannot play that card. Choose another.")
