'''
Player class
'''
from Hand import Hand

class Player:

    def __init__(self,name,balance=100):
        self.name = name
        self.hand = Hand()
        self.balance = balance
        self.bet = 0
    
    def win(self):
        self.balance += self.bet
        print (f'New balance is {self.balance}')
    
    def lose(self):
        self.balance -= self.bet
    
    def bet_amount(self,bet):
        self.bet = bet

    def __str__(self):
        return f'Player Name: {self.name}\nPlayer Balance: {self.balance}'
