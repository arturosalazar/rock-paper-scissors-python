from random import randint

#Game Start Loop
keepPlaying = True
while (keepPlaying):
    #Randomly select 
    computerPossibleMoves = ("Rock", "Paper", "Scissors")
    computerMove = computerPossibleMoves[randint(0,2)]
    #Test - select specific computerMove
    computerMove = "Scissors"

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
    
    #Compare the user's choice with the computer's choice to determine the winner.
    #Tie Condition
    if userMove == computerMove:
        print("It's a tie!")

    #Player Chooses Rock
    elif userMove == "Rock":
        if computerMove =="Scissors":
            print(f"You win! {userMove} smashes {computerMove}")
        elif computerMove == "Paper":
            print(f"Computer wins! {computerMove} covers {userMove}")
    #Player Chooses Paper
    elif userMove == "Paper":
        if computerMove =="Rock":
            print(f"You win! {userMove} covers {computerMove}")
        elif computerMove == "Scissors":
            print(f"Computer wins! {computerMove} cuts {userMove}")
    #Player Chooses Scissors
    elif userMove == "Scissors":
        if computerMove =="Paper":
            print(f"You win! {userMove} cuts {computerMove}")
        elif computerMove == "Rock":
            print(f"Computer wins! {computerMove} smashes {userMove}")