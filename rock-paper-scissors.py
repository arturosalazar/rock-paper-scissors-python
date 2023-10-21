from random import randint

#Randomly select 
computerPossibleMoves = ("Rock", "Paper", "Scissors")
computerMove = computerPossibleMoves[randint(0,2)]
print(computerMove)

#Game Start Loop
keepPlaying = True
while (keepPlaying):
    #Select a move 
    userMove = input("Select a move: Rock, Paper, Scissors: ")
    print(userMove)

    #Convert move to avoid formatting problems
    userMove = userMove.lower() #make lowercase
    userMove = userMove.title() #capitalize first letter
    userMove = "".join(userMove.split()) #remove all whitespace
    print(userMove)

    #Check user input
    if userMove not in ["Rock", "Paper", "Scissors"]:
        print("Incorrect Selection, try again")
        continue

    print("Computer selected: " + computerMove.title())
    print("User selected: " + userMove.title())

    