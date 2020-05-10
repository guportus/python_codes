'''
Hand Class
'''

from Card import Card
from Deck import Deck

class Hand:
    
    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.adjust_for_ace()

    def adjust_for_ace(self):
        self.value = 0
        for card in self.cards:
            self.value += Deck.values[card.rank]
            if card.rank == 'Ace' and self.value > 21:
                self.value -= 10
            
                
    def init_cards(self):
        self.cards = []
        self.value = 0
        self.aces = 0

