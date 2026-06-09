#Take input for the student that he can attend the exam or not
medical_cause = input("Did you have a medical cause yes or no?:")
#Take input of the attendance
attendance = int(input("Enter the attendance of the student:"))

#Checking the user input predicting output accordingly

if medical_cause == "yes":
    print("You are allowed to give the exam.")
else:
    if attendance>=75:
        print("Allowed")
    else:
        print("Not allowed")