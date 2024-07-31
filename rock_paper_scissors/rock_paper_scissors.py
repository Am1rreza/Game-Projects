import random

computer_win = 0
user_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        print("Invalid choice, please choose again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You Won!")
        user_win += 1
    else:
        print("You Lost!")
        computer_win += 1

print(f"\nFinal Scores:\nComputer won {computer_win} times\nYou won {user_win} times")
print("Goodbye!")