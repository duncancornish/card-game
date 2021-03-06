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

    def checkplayable(self):#Returns True if the card can be played, otherwise returns False
        playable=False
        if self.val==10 or playpile.cards==[] or self.val==1 or self.val==2 or (self.val >= playpile.cards[-1].val and playpile.cards[-1].val!=1):
            playable=True
        return playable

class Deck:
    def __init__(self):
        self.cards=[]
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:#Assembles the deck
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

    def play(self, card):
        if card.val==10:#Lets 10 remove all cards in the pile from play
            playpile.cards=[]
        else:
            playpile.cards.append(card)
        self.cards.remove(card)
        if deck.cards!=[] and len(self.cards)<4:
            self.draw()
playpile=Hand()

class Player:
    def __init__(self):
        self.hand=Hand()
        self.frontdown=Hand()
        self.frontup=Hand()
        for i in range(3):#Creates the starting hand and arranges the other 6 cards needed
            self.hand.draw()
            self.frontup.draw()
            self.frontdown.draw(faceup=False)


    def show(self):#SHows the hand, then the face-up cards in front, then how many face-down cards there are in front
        print("Hand:")
        for card in self.hand.cards:
            card.show()
        print("In front:")
        for card in self.frontup.cards:
            card.show()
        for card in self.frontdown.cards:
            card.show()

    def checkplayable(self):#Returns True if there is a card the player can play right now, otherwise returns False (unless they only have face-down cards left)
        playable=False
        if len(self.hand.cards)>0:
            for card in self.hand.cards:
                if card.val==10 or playpile.cards==[] or card.val==1 or card.val==2 or (card.val >= playpile.cards[-1].val and playpile.cards[-1].val!=1):
                    playable=True
        elif len(self.frontup.cards)>0:
            for card in self.frontup.cards:
                if card.val==10 or playpile.cards==[] or card.val==1 or card.val==2 or (card.val >= playpile.cards[-1].val and playpile.cards[-1].val!=1):
                    playable=True
        elif len(self.frontdown.cards)>0:#With only face-down cards left, this just tries to play one of the cards now
            print("Attempting to play a card...")
            card=self.frontdown.cards[0]
            card.faceup=True
            print("Card is "+card.show())
            if card.val==10 or playpile.cards==[] or card.val==1 or card.val==2 or (card.val >= playpile.cards[-1].val and playpile.cards[-1].val!=1):
                self.frontdown.play(card)
                playable=0
            else:#If the card cannot be played, it then goes to the hand
                self.hand.cards.append(card)
                self.frontdown.cards.remove(card)
                playable=0
        return playable

    def checkvictory(self):#Returns True if the player has no cards in their hand or in front of them, otherwise returns False
        if len(self.hand.cards)==0 and len(self.frontup.cards)==0 and len(self.frontdown.cards)==0:
            return True
        else:
            return False

players={}
pcount=input("How many players? ")
if int(pcount)>5:#Not enough people for the deck to cover
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
        playable=players[p].checkplayable()
        if playable==False:
            input("No cards currently playable, attempting to draw a card and skipping the turn...")
            if deck.cards!=[]:
                players[p].hand.draw()
        elif playable==True:
            cardhasbeenplayed=False
            while cardhasbeenplayed==False:
                playcard=input("Which card would you like to play? ")
                playcard=int(playcard)-1#Counters python's tendancy of labelling the first element of a list the 0th element, since people aren't going to pick the 0th card
                if len(players[p].hand.cards)>0:#Conditional to select where the card is coming from
                    playcard=players[p].hand.cards[playcard]
                elif len(players[p].frontup.cards)>0:
                    playcard=players[p].frontup.cards[playcard]
                else:
                    playcard=players[p].frontdown.cards[0]
                if playcard.checkplayable()==True:#If it can be played, plays it
                    players[p].hand.play(playcard)
                    cardhasbeenplayed=True
                else:#Otherwise, makes the player go back and choose again
                    print("You cannot play that card. Choose another.")
        if players[p].checkvictory():#If a player has no cards in their hand or in front of them, they are the winner and the game is over
            print("Player "+str(p+1)+" has no cards left! They are the winner!")
            gameover==True
