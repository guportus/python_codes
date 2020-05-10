'''
Deck Class
'''
import random
from Card import Card

class Deck:
# CLass deck
    suits = ('Hearts', 'Diamond', 'Spades', 'Club')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten', 'Jack','Queen','King','Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
                'Queen':10,'King':10,'Ace':11}

    #Create the deck
    def __init__(self):
        print('Creating Deck of Cards')
        self.deck = []

        for suit in self.suits:
            #print (f'Suits :' + suit)
            for rank in self.ranks:
                self.deck.append(Card(suit,rank))

        print (f'{len(self.deck)} cards created')        
    
    #Shuffle the Cards
    def shuffle(self):
        random.shuffle(self.deck)

    def give_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card
    
    #Print decks of Cards
    def __str__(self):
        str_card = ""
        for card in self.deck:
            str_card = str_card + card.rank + ' of ' + card.suit + '\n'
        
        return str_card

    