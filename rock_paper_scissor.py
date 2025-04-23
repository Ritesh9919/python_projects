import random

you_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    if user_input == "q":
        break
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0,2)
    computer_choice = options[random_number]
    print(f"Computer chose {computer_choice}")

    if user_input == "rock" and computer_choice == "scissors":
        print("You win!")
        you_win += 1
    elif user_input == 'paper' and computer_choice == 'rock':
        print("You win!")
        you_win += 1
    elif user_input == 'scissors' and computer_choice == "paper":
        print("You win!")
        you_win += 1
    else:
        print("You lose!")
        computer_win += 1

print(f"You won {you_win} times ")
print(f"Computer won {computer_win} times")
print("Goodbye!")                    




