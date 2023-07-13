from random import randint

user_wins = 0
computer_wins = 0
play_options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock\paper\scissors to play or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in play_options:
        continue

    random_number = randint(0, 2)
    # rock == 0, paper == 1, scissors == 2

    computer_pick = play_options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    if user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    if user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("You and computer are even, so no one wins this time.")

    else:
        print("Computer wins this time.")
        computer_wins += 1

print(f"You won {user_wins} times.", f"The computer won {computer_wins} times", "Goodbye!", sep="\n")