#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Milestone project
#TicTacToe

#Use jupyter library to clear output
from IPython.display import clear_output

#Import Random
import random
#import string
import string

#Ask player one if marker is X or O
def player_marker():
    
    marker=''
    player1='X'
    player2='O'
    
    while marker.upper() != 'O' and marker.upper() != 'X':
            
        marker = input('Player 1, choose X or O : ')
        
        if marker.upper() != player1:
            player1='O'
            player2='X'
        
    return (player1,player2)
            

#Select random if player 1 or player 2 to go first
def goes_first():
    
    return random.randint(1,2)
    
#Display Tic Tac Toe Board    
def display_board(board, clear=False):
    #clear output
    if clear:
        clear_output()
    
    #printout the board
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    

#Place marker X or O on the board
def place_marker(board, position, marker):    
    board[position-1] = marker

#Check if board is full
def board_full():
    return board.count('X') + board.count('O') == 9
    
#Check if a player already wins
def check_win(board,mark):
    
    if (board.count(mark)) < 3:
        return False
    
    win = False
    
    for pos in range(0,9):
    
        if pos == 0 and (board[0] == board[1] == board[2] == mark or board[0] == board[3] == board[6] == mark or board[0] == board[4] == board[8] == mark):
            win = True
        elif pos == 1 and (board[1] == board[4] == board[7] == mark):
            win = True
        elif pos == 2 and (board[2] == board[5] == board[8] == mark or board[2] == board[4] == board[6] == mark):
            win = True
        elif pos == 3 and board[3] == board[4] == board[5] == mark:
            win = True
        elif pos == 6 and board[6] == board[7] == board[8] == mark:
            win = True
        
        if win:
            break

            
    return win

# Ask player for a position
def enter_position(player,board):
    
    exist = True
    while exist:
        position = 'x'
        while position not in ('123456789'):
            position = input(f"Player{player} Enter a position from 1 - 9")
        position = int(position)
        if board[position-1] == ' ':
            exist = False
        else:
            print(f"Position {position} already taken")
        
    return position

#Ask if wants to play again
def play_again():
    
    again = 'x'
    while again.upper() not in ('YN'):
        again = input("Do you want to play again [Y/N] : ")
    
    if again.upper() == 'Y':
        return True
    else:
        return False

#welcome message
print("Welcome to TIC TAC TOE")


board = [1,2,3,4,5,6,7,8,9]
display_board(board)

#Player 1 choose X or O
player1_marker, player2_marker = player_marker()

player_marker = {'p1':player1_marker,'p2':player2_marker}

print(f"Player 1 chooses: {player_marker['p1']}. Player 2 will take {player_marker['p2']}")

first = goes_first()

player1 = True

if first == 2:
    player1=False

print(f'First player to go is Player {first}')

#initialize the board
game = True
while game:
    board = [' ']*9
    clear=True
    display_board(board)

    full = board_full()
    win = check_win(board,player1_marker)

    while not full and not win:

          clear=True
          if player1:
              position = enter_position(1,board)
              place_marker(board,position,player1_marker)
              display_board(board,clear)
              win = check_win(board,player1_marker)
              if win:
                  print("Player 1 wins")
                  
              full = board_full()
              player1 = False
          else:
              position = enter_position(2,board)
              place_marker(board,position,player2_marker)
              display_board(board,clear)
              win = check_win(board,player2_marker)
              if win:
                  print("Player 2 wins")
                  
              full = board_full()
              player1 = True

          if full:
              print("Board is full")
    
    game = play_again()
      
print("Thank you for playing TIC TAC TOE by Geri")


# In[ ]:




