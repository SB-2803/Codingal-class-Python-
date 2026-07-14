def shutdown():
    print("Shutting down!!")
    
answer = input("Do you want to shutdown your laptop: ")
while answer not in("yes","Yes","No","no"):
    print("Invalid input!!")
    answer = input("Do you want to shutdown your laptop: ")
if answer == "Yes" or answer == "yes":
    shutdown()
elif answer == "No" or answer == "no":
    print("You are not ready to shutdown!")
        
