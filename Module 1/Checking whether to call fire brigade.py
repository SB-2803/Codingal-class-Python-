name = input("Enter your name:")
print("Today we will check whether you should call the fire brigade or not. To do please fill the following:")
fire = input("Enter yes if you can see fire flames:")
cooking = input("Enter yes if there is flame cooking going on in your house:")
if fire == "yes" and cooking == "yes":
    print(name,"you don't need to call a fire brigade. YOU ARE SAFE!!!!")
elif fire == "yes" and cooking == "no":
    print(name,"immediately call a fire brigade. YOU ARE IN DANGER!!!")
elif fire == "no" and cooking == "no":
   print(name,"you don't need to call a fire brigade. YOU ARE SAFE!!!!")
elif fire == "no" and cooking == "yes":
   print(name,"you don't need to call a fire brigade. YOU ARE SAFE!!!!")