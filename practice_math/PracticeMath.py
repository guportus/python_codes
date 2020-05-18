import Display
import random
from functools import reduce
from Utility import sort_reverse
import time

def select_menu():

    while True:
        
        choice = input("Enter Math Operation you want to practice : ")

        if choice.upper() in ['A','B','C','D']:
            return choice.upper()
        else:
            print("Please choose from A-B")


def gen_numbers(high,size=2):
    numbers = []
    
    for i in range(size):
        numbers.append(random.randint(1,high))

    return numbers

def get_answer(question):

    while True:
        try:
            ans = int(input(question))
            return ans
        except:
            print("Please input a number")
            continue

def substract(numbers):
    return reduce(lambda x,y: x-y,numbers)      

def multiply(numbers):
    return reduce(lambda x,y: x*y,numbers)   

def divide(numbers):
    return reduce(lambda x,y: x/y,numbers)   


def math_operation(numbers, operation):
    
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        return substract(numbers)
    elif operation == '*':
        return multiply(numbers)
    else:
        return divide(numbers)



if __name__ == '__main__':

    while True:
        Display.display_welcome()

        choice = select_menu()
        oper = {'A':'+','B':'-','C':'*','D':"/"}
        

        no_questions = get_answer("Enter number of questions : ")
        high = get_answer("Enter the high number : ")
        right = 0
        wrong = 0

        Display.clear_screen()

        for i in range(no_questions):
            Display.clear_screen()
            #Get Random number
            numbers = sort_reverse(gen_numbers(high))
            #Display the equation
            print(f"   Question {i+1} of {no_questions}\n")
            Display.display_ques_vert(numbers,oper[choice])

            #Get the users input from answers and check if the answer is correct
            if (get_answer("   ") == math_operation(numbers, oper[choice])):
                print("\n   You got it right")
                right += 1
            else:
                print("\n   Sorry Wrong answer")
                wrong += 1

            #print(f"\n   Correct Ans: {right}. Wrong Ans {wrong}\n")
            time.sleep(2)

        #Display scores
        if (no_questions == right):
            print(f"   You get a perfect score!!! {right} of {no_questions}")
        else:
            grade = (right / no_questions) * 100
            print(f"   Your grade is {grade:0.2f}. {right} of {no_questions}")

        
        
        cont = input("   Press Y if you want to start again : ")

        if cont.upper() == 'Y':
            continue
        else:
            break
    
    Display.display_thank()
        

    