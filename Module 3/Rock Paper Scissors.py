import random

options = ["Rock", "Paper", "Scissors"]
user_choice = input("Choose Rock, Paper or Scissors:")
comp_choice = random.choice(options)

print("You choose:",user_choice)
print("Computer chooses:",comp_choice)

if user_choice == comp_choice:
    print("It's a tie!!")
elif user_choice == "Paper" and comp_choice == "Rock":
    print("Paper covers rock!! You win!!")
elif user_choice == "Scissors" and comp_choice == "Paper":
    print("Scissors cuts paper!! You win!!")
elif user_choice == "Rock" and comp_choice == "Scissors":
    print("Rock smashes scissors!! You win!!")
else:
    print("You lose!")