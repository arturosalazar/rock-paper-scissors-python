from random import randint

#Randomly select 
computerPossibleMoves = ("rock", "paper", "scissors")
computerMove = computerPossibleMoves[randint(0,2)]
print(computerMove)

#Game Start Loop
keepPlaying = True
while (keepPlaying):
    #Select a move 
    userMove = input("Select a move: r, p, s: ")
    print(userMove)