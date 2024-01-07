import random

option = {
    'rock': False,
    'paper': False,
    'scissors': False
}

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
        option['rock'][True]
        break
    elif option == 'paper' or option == 'p':
        option['paper'][True]        
        break
    elif option == 'scissors' or option == 's':
        option['scissors'][True]
        break
    
    
