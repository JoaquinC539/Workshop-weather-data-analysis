import random

print('Welcome!')

def main():
    numsChosen = []
    count = 0
    hint = 3

    #Machine will chose random number between 1 - 50

    machineChoice = random.choice(range(1,51))
    print('')

    while True:
    
        # if hint <= 0:
        #     print('No hints available')
        if hint > 0:
            print(f'Hints available: {hint}')
    # Begin Prompt
        guess = input('Please guess a number between 1 and 50 (blank to exit):\n')
        if validate_input(guess) == True:
            guess = int(guess)
            # If number found, end game
            if guess == machineChoice:
                print('You won!')
                count += 1
                break

            else:
                count += 1
                numsChosen.append(guess)
                print('Incorrect Number')
                print(f'guesses so far: {numsChosen}\n')
                continue
        elif guess == 'hint': ########## HERE ##########
            give_hint(str(machineChoice), hint)
            hint -= 1
        elif guess == '':
            break

        else:
            print('Invalid Input, please try again\n')
            continue

    print('\n************ RESOLUTIONS ************\n')
    print(f"Machine's Choice: {machineChoice}\n")
    print(f'Number of attempts: {count}\n')
    if len(numsChosen) >= 1:
        print(f'Numbers Used: {numsChosen}\n')
    else:
        print('Numbers Used: First Try!!\n')
    if hint <= 0:
        print('All hints were used\n')
    else:
        print(f'Hints used: {3 - hint}\n')

def validate_input(userInput):
    if userInput.isdigit() and (int(userInput) >= 1 and int(userInput) <= 50) and (userInput != '') and (userInput != 'hint'):
        return True
    else:
        return False

def give_num_value(machineNum):
    if machineNum == '1':
        return 'one'
    elif machineNum == '2':
        return 'two'
    elif machineNum == '3':
        return 'three'
    elif machineNum == '4':
        return 'four'
    elif machineNum == '5':
        return 'five'
    elif machineNum == '6':
        return 'six'
    elif machineNum == '7':
        return 'seven'
    elif machineNum == '8':
        return 'eight'
    elif machineNum == '9':
        return 'nine'


def give_hint(machineNum, hintChance):
    
    if hintChance == 3:
        digits = len(machineNum)
        print(f'The number has {str(digits)} digit(s)\n')
    if hintChance == 2:
        if len(machineNum) == 2:
            print(f'The first digit of the number starts with the letter "{machineNum[0]}"\n')
        else:
            word = give_num_value(machineNum)
            print(f'The first letter of the number is {word[0]}\n')
    if hintChance == 1:
        x = machineNum[0]
        word = give_num_value(x)
        print(f'The first digit of the number starts with  "{word[0]}{word[1]}"\n') 

    if hintChance <= 0:
        hintChance == 0
        print('You have no more hints left!\n')

def try_again():
    again = input('Do you wish to paly again? y for yes, n for no.\n')
    if again == 'y' or again == 'yes' or again == 'yeah':
        return True
    else:
        return False
#________________________________________________________________________________________________________________________________________________________________#

main()
while True:
    if try_again() == True:
        main()
    else:
        print('Goodbye!')
        break