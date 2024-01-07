from random import choice

options=["rock","paper","scissors"]

print("Welcome to rock, paper, scissors game")
playAgain = True

while playAgain:
    option = input('Please select an option... "Rock", "Paper" or "Scissors"...').lower()

    if(option.lower() not in options):
        continue

    machine_selection = choice(options)
    print(machine_selection)
    
    if(option == machine_selection):
        print("TIE!")
    elif(option=="rock" and machine_selection=="scissors"):
        print("You win")
    elif(option=="paper" and machine_selection=="rock"):
        print("You win")
    elif(option=="scissors" and machine_selection=="paper"):
        print("You win")
    else:
        print("Python wins")

    playAgain=input("\nPlay again? \n Y for yes or Q to quit\n\n")
    if (playAgain.lower()=="y" or playAgain.lower()=="yes"):
        continue
    else:
        print("Thanks for playing")
        playAgain=False

