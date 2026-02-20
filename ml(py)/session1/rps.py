import random

def play_game():
    rps = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("Enter rock, paper or scissors: ").lower()
        
        if player_choice not in rps:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(rps)

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")

        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")

        else:
            print("You lose!")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

play_game()