import random
from helperFunctions import printQuestion, checkAnswer, clearScreen
import time

clearScreen()

allowedOperations = ['+', '-', '*', '/']
operations = []

print("hi")

# initialise variables
print("BOotinG ZZZzZZZzzzzzzzZZzetamax")
print("\n")
print("Press any key to start.")
input()

# user chooses the operations they would like to include
try_again = 0
while True:
    clearScreen()
    print("Type q to quit.")
    print("\n")
    print("Choose your desired operations.\nTo do so, please type in '+', '-', '*' or '/' separated by spaces for your corresponding desired operations.")
    
    if try_again:
        print("No operation registered. Try again.")
    
    user_operations = input().split(" ")

    if not user_operations: 
        try_again = 1
        continue

    if 'q' in user_operations:
        exit()

    for i in range(len(user_operations)):
        if user_operations[i] in allowedOperations:
            operations.append(user_operations[i])

    if not operations:
        try_again = 1
        continue
    
    break

# now set desired time limit

try_again = 0
while True:

    clearScreen()
    print("Type q to quit.")
    print("\n")
    print("Set your desired time limit:")

    if try_again == 1:
        print("Invalid time limit. Please enter a positive integer.")

    time_limit = input()

    if time_limit == 'q':
        exit()

    if not time_limit.isdigit():
        try_again = 1
        continue
    else:
        time_limit = int(time_limit)
    
    if time_limit <= 0:
        try_again = 1
        continue
    else:
        break

score = 0
playing = 1
q_num = 0
prev_q_num = -1

time_end = time.time() + time_limit
wrong = 0
invalid = 0

# start game
while time.time() < time_end:

    # reset the screen
    clearScreen()
    print("Type q to quit.")
    print("\n")

    # if the previous input was invalid or wrong let them know
    if prev_q_num == q_num:
        printQuestion(n1, n2, operation) 
        if invalid:
            print("Invalid input. Try again.")
        elif wrong:
            print("Incorrect answer. Try again.")
    else:
        prev_q_num = q_num

        # generate operation
        operation = operations[random.randint(0, len(operations) - 1)]

        # generate random numbers
        if operation == '/':
            n2 = random.randint(0,100)
            n1 = random.randint(0,10) * n2
        else:
            n1 = random.randint(0,100)
            n2 = random.randint(0,100)

        printQuestion(n1, n2, operation)

    
    user = input()

    if user == 'q':
        exit()

    try:
        user = int(user)
    except ValueError:
        invalid = 1
        continue

    # check the given answer
    if checkAnswer(user, n1, n2, operation):
        score += 1
    else:
        wrong = 1
        continue

    q_num += 1
    wrong = 0
    invalid = 0

# reset the screen
clearScreen()
print("You got a score of " + str(score) + ". Do better.")
