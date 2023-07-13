import random

top_of_range = input("Write a maximum number in current game: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please, next time type number large than 0.")
        quit()
else:
    print("Please, print number next time.")
    quit()

random_number = random.randint(0, top_of_range)
try_guesses = 0

while True:
    try_guesses += 1
    current_user_guess = input("Make a guess: ")
    if current_user_guess.isdigit():
        current_user_guess = int(current_user_guess)
    else:
        print("Please type number next time")
        continue
    if current_user_guess == random_number:
        print("You got this!")
        break
    else:
        if current_user_guess > random_number:
            print("You were above the number this time.")
        else:
            print("You were below the number this time.")

print(f"You got this in {try_guesses} guesses!")