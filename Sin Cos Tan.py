import math
angle = int(input("Enter any angle:"))
if angle >= 0:
  print("Sin value is:",math.sin(angle))
  print("Cos value is:",math.cos(angle))
  print("Tan value is:",math.tan(angle))
else:
  print("Angle should be positive for this function!!")