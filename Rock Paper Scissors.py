game_init = input("Press Y to start the game : ").upper()
while game_init == "Y":
    print("Enter both player's choices : ")
    player1 = input("Player 1, choose from Rock Paper Scissors : ").upper()
    player2 = input("Player 2, choose from Rock Paper Scissors : ").upper()

    if player1 == "ROCK" and player2 == "SCISSORS":
        print("Player1 Wins!!")
    elif player1 == "ROCK" and player2 == "PAPER":
        print("Player2 Wins!!")
    elif player1 == "PAPER" and player2 == "ROCK":
        print("Player1 Wins!!")
    elif player1 == "PAPER" and player2 == "SCISSORS":
        print("Player2 Wins!!")
    elif player1 == "SCISSORS" and player2 == "ROCK":
        print("Player2 Wins!!")
    elif player1 == "SCISSORS" and player2 == "PAPER":
        print("Player1 Wins!!")
    elif player1 == player2:
        print("It's a Tie!!")
    else:
        print("Invalid choice")
    game_init = input("Press Y to play again and Q to quit ").upper()
    if game_init == "Q":
        break

print("Thank you for playing")
