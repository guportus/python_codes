'''
Create Display
'''
import os
import subprocess

def clear_screen():
    os.system('cls')
    subprocess.call("cls",shell=True)

def display_welcome():
    clear_screen()
    size = 80
    
    print('*' * size)
    printer(size,'*','Welcome to Math Practice')
    printer(size,'*','')
    print('*' * size)
    printer(size,'*','')
    printer(size,'*','[A] Addition        ')
    printer(size,'*','[B] Substraction    ')
    printer(size,'*','[C] Mulitiplication ')
    printer(size,'*','[D] Division        ')
    printer(size,'*','')
    print('*' * size)


def printer(size, char, message):
    message_len = len(message)

    space1 = int((size - message_len) / 2) -1
    space2 = size - space1 - message_len - 2

    print(char + (' ' * space1) + message + (' ' * space2) + char)

def display_question(numbers, operation):

    size = len(numbers)

    numwords = '' + str(numbers[0])

    for i in range(1,size):
        numwords = numwords + ' + ' + str(numbers[i])
    
    numwords = numwords + ' = ' 

    print (numwords)


def display_ques_vert(numbers, operation):

    size = len(numbers)

    print('   ' + str(numbers[0]))

    for i in range(1,size):
        print('   ' + operation)
        print('   ' + str(numbers[i]))
     

    print ("   -----")

def display_thank():
    clear_screen()
    size = 80

    print('*' * size)
    printer(size,'*','')
    printer(size,'*','')
    printer(size,'*','Thank you for using Practice Math')
    printer(size,'*','')
    printer(size,'*','By : Geri Portus')
    printer(size,'*','')
    printer(size,'*','')
    print('*' * size)