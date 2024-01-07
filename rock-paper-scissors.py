########### Algoritmo ###########
#1. Variables de valores e importar modulo para escoger una opción random
#2. Preguntar al usuario su opción
#3. Escoger de las variables para comparar la opción del; usuario
#4.1 Para compara poner la opciones en boolean
#4.2 Comparar la opciones
#5 Definr ganador

from random import choice

playerWins = False
draw = False

print('Welcome to rock, paper, scissors game')

while True:

    selections = ["rock","paper","scissors"]

    machineSelection = choice(selections)

    option = input('Please select an option... "Rock", "Paper" or "Scissors"...\n')

    if option.lower() not in selections:
        print('invalid selection. Please try again... ')
        continue

    else:
        option = option.lower()
    
        if option == 'rock' and machineSelection == selections[0]:
            draw = True
        if option == 'rock' and machineSelection == selections[1]:
            playerWins = False
        if option == 'rock' and machineSelection == selections[2]:
            playerWins = True
        
        if option == 'paper' and machineSelection == selections[0]:
            playerWins = True
        if option == 'paper' and machineSelection == selections[1]:
            draw = True
        if option == 'paper' and machineSelection == selections[2]:
            playerWins = False
        
        if option == 'scissors' and machineSelection == selections[0]:
            playerWins = False
        if option == 'scissors' and machineSelection == selections[1]:
            playerWins = True
        if option == 'scissors' and machineSelection == selections[2]:
            draw = True

        if draw == True:
            print("It's a tie!")
        if playerWins == True:
            print('You won!')
        elif playerWins == False:
            print('You lost')
        break
    



        
    
    
    
