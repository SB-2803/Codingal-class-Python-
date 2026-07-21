import random #importing module
playing = True
num = str(random.randint(10,20))

print("A number between 10 to 20 will be generated and you have to guess the number.")
print("The game ends when you get the correct guess!!")
while playing:
    guess = input("Give me your best guess!! \n")
    if num == guess:
        print("You win the game!!")
        print("The number was",num)
        break
    else:
        print("You guess isn't quite right. Try agin!!")