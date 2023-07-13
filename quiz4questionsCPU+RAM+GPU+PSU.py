print("Welcome to my simple computer quiz!")

playing_status = input("Do you want to play? (yes/no) ")

if playing_status.lower() != "yes":
    quit()

print("Okay, let's play! There will be 4 questions, so answer correctly :')")

users_points = 0

answer = input("Question 1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    users_points += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    users_points += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 3. What does RAM stand for? ")
if answer.lower() == "random access memory":
    users_points += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 4. What does PSU stand for? ")
if answer.lower() == "power supply unit":
    users_points += 1
    print("Correct!")
else:
    print("Incorrect!")


print(f"You got {users_points} questions correct! Congratulations) That's a {(4/users_points)*100}%.")