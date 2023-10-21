from random import randint

#Randomly select 
computerPossibleMoves = ("rock", "paper", "scissors")
computerMove = computerPossibleMoves[randint(0,2)]
print(computerMove)

#Game Start Loop
keepPlaying = True
while (keepPlaying):
    #Select a move 
    userMove = input("Select a move: r for Rock, p for Paper, s for Scissors: ")
    print(userMove)

    #Convert move to avoid formatting problems
    userMove = userMove.lower() #make lowercase
    userMove = "".join(userMove.split()) #remove all whitespace
    print(userMove)

    #Check user input
    if userMove not in ["r", "p", "s"]:
        print("Incorrect Selection, try again")
        continue

