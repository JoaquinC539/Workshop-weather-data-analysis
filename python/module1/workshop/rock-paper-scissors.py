from random import choice
from pdb import set_trace as bp

playerWins = False
draw = False

print('\nWelcome to rock, paper, scissors game!')

while True:

    selections = ["rock","paper","scissors"]
    
    machineSelection = choice(selections)
    # bp()
    option = input('\nPlease select an option... "Rock", "Paper" or "Scissors"...\n')

    if (option.lower() not in selections) and option != '':
        print('invalid selection. Please try again... ')

    if option == '':
        print('Goodbye!\n')
        break

    else:
        option = option.lower()
        
        print(f'\nYou have selected {option.upper()}!')
        print(f'Machine has selected {machineSelection.upper()}!\n')

        if option == machineSelection:
            draw = True
        if option == 'paper' and machineSelection == selections[0]:
            playerWins = True
        if option == 'scissors' and machineSelection == selections[1]:
            playerWins = True
        if option == 'rock' and machineSelection == selections[2]:
            playerWins = True
        else:
            playerWins = False

        if draw == True:
            print("It's a tie!")
        elif playerWins == True:
            print('You won!')
        elif playerWins == False:
            print('You lost')

        playAgain = input('Do you wish to play again?\n')
        playAgainOptions = ['yeah', 'yes', 'y', 'play']
        playAgain = playAgain.lower()

        if playAgain in playAgainOptions:
            continue
        else:
            print('Goodbye!\n')
            break