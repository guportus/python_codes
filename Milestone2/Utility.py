'''
This are utilities
'''
import os
import subprocess
from colorama import Fore

def clear_screen():
    os.system('cls')
    subprocess.call("cls", shell=True)

def display_table(dealer, player, show=False):
    display_welcome()
    print(Fore.RED)
    print('Dealers Hand')
    cnt = 1
    for card in dealer:
        if show and cnt >= 2:
            print('Second Card')
            break
        print(card)
        cnt += 1


def display_card(dealer, player, show=False):
    display_welcome()
    print(Fore.RED)
    print('Dealers Hand')
    
    for card in dealer.cards:
        print(card)
        if not show:
            print ("Second Card")
            break
    
    if show:
        print(f"Dealer Value : {dealer.value}")


    print(Fore.BLUE + "\n\n")
    print("Players Hand")
    
    for card in player.hand.cards:
        print(card)
    
    value = player.hand.value
    print(f"Player Count : {value}" )


def display_welcome():
    clear_screen()
    border = '*' * 55
    print(Fore.GREEN + border)
    print('*       W E L C O M E   T O   B L A C K J A C K       *')
    print(Fore.GREEN +border)

def display_thanks():
    clear_screen()
    border = '*' * 55
    print(Fore.GREEN + border)
    print('*                  T H A N K   Y O U                  *')
    print('*                                                     *')
    print('*            B Y :   G E R I   P O R T U S            *')
    print(Fore.GREEN +border)