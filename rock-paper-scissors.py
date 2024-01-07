import random


rock = [False, 1]
paper = [False, 2]
scissors = [False, 3]


# Rock = False
# Paper = False
# Scissors = False

while True:
    userContinue = input('Welcome to rock, paper, scissors game. Please hit "Return" to continue...')
    if userContinue == '':
        break
    else:
        pass

while True:
    option = input('Please select an option... "Rock", "Paper" or "Scissors"...')
    option = option.lower()
    if option == 'rock' or option == 'r':
        rock[0] = True
        break
    elif option == 'paper' or option == 'p':
        paper[0] = True      
        break
    elif option == 'scissors' or option == 's':
        scissors[0] = True
        break
    else:
        print('please select a valid option...')

#print(random.choice(option[])
    
