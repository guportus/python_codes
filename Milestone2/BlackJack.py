from Deck import Deck
from Hand import Hand
from Player import Player
import time
import os
import Utility

playing = True

def take_bet(balance):
    
    while True:

        try:
            bet = int(input("Place your bet : "))

            if bet > balance:
                print("You dont have enough money")
                continue
        except:
            print("Kindly enter a number")
        else:
            break
    return bet       

def hit(deck, hand, dealer=False):
    hand.add_card(deck.give_card())
    
    ans = True

    if hand.value > 21:
        print ("Bust")
        ans = False
    playing = ans
    return playing

def hit_stand():
    
    x = 'x'

    while x not in ('HS'):
        x = input("Enter H for Hit or S for Stand : ")

        if x.upper() == 'H':
            return True
        elif x.upper() == 'S':
            return False
        else:
            continue

def cont_play():

    while True:

        x = input("Do you want to continue playing [Y/N] : ")

        if x.upper() == 'Y':
            return True
        elif x.upper() =='N':
            return False
        else:
            continue

if __name__ == '__main__':
    
    #Display welcome message
    Utility.display_welcome()

    #Ask Player name
    name = input('Enter your name : ')

    Utility.display_welcome()
    
    print (f"Hello {name} \n\n\nHere is your initial balance")
    
    dealer = Hand()
    player = Player(name,200)
    print(player)

    while True:
        #Create deck of Card
        deck = Deck()
        
        #shuffle the card
        deck.shuffle()
        
        #Display welcome message
        Utility.display_welcome()


        #Initialize hands cards
        dealer.init_cards()
        player.hand.init_cards()

        print ("Player place your bet")
        print(player)
        print("\n\n")
        player.bet_amount(take_bet(player.balance))

        print("Giving cards....")
        time.sleep(1.5)
        #Start of the game. Card is give to player and dealer
        #Player first Card
        player.hand.add_card(deck.give_card())

        Utility.display_card(dealer,player)
        #delay 2 secs
        time.sleep(2)
        
        #Dealer First Card
        dealer.add_card(deck.give_card())
        Utility.display_card(dealer,player)
        time.sleep(2)
        
        #Player Second Card
        player.hand.add_card(deck.give_card())
        Utility.display_card(dealer,player)
        #time.sleep(3)

        #Dealer Second Card but will not be shown
        dealer.add_card(deck.give_card())
        Utility.display_card(dealer,player)
        
        #Ask the player to hit or stand
        take_card = False

        player_value = player.hand.value
        dealer_value = dealer.value
        bust = False
        dealer_bust = False
        playing = True
        #Player turn
        while playing:
            playing = hit_stand()

            if playing:
                player.hand.add_card(deck.give_card())
                player_value = player.hand.value
                Utility.display_card(dealer,player)

                if player_value > 21:
                    bust = True
                    print ("Player BUST")
                    break
                else:
                    continue
                
        #Dealers Turn
        Utility.display_card(dealer,player,True)
        
        while True and not bust:
            print("Dealers Turn")
            if dealer_value >= 17:
                break

            dealer.add_card(deck.give_card())
            dealer_value = dealer.value
            Utility.display_card(dealer,player, True)
            if dealer_value > 21:
                dealer_bust = True
                break
            elif dealer_value >= 17:
                break
            else:
                continue
        

        if bust:
            print(f"Dealer WINS {dealer_value}! Player BUST")
            player.lose()
        elif dealer_bust:
            print(f"Player WINS {player_value}! Dealer BUST")
            player.win()
        elif dealer_value > player_value:
            print(f"Dealer WINS {dealer_value}! Player lose {player_value}")
            player.lose()
        elif player_value > dealer_value:
            print(f"Player WINS {player_value}! Dealer lose {dealer_value}")
            player.win()
        else:
            print ("PUSH")
        
        if cont_play():
            if player.balance > 0:
                continue
            else:
                print("Sorry you dont have any money")
                time.sleep(2)
                break
        else:
            break



    print(player)
    time.sleep(3)
    Utility.display_thanks()




    
    