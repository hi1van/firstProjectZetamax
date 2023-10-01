import os

def printQuestion(n1, n2, operation):
    print(n1, operation, n2, "=")

def checkAnswer(user, n1, n2, operation):
    
    if operation == '+':
        if user == n1 + n2:
            return 1
    elif operation == '-':
        if user == n1 - n2:
            return 1
    elif operation == '*':
        if user == n1 * n2:
            return 1
    elif operation == '/':
        if user == n1 / n2:
            return 1
        
    return 0

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')