habit = ("Studying", 7, 120)
print("My Weekly Habit Tracker!!!!")
print("\nHabit Name:", habit[0])

record = (1, 1, 1, 0, 1, 0, 1)
print("Weekly Record:", record)
print("Total number of days the habit was recorded:", len(record))
print("Amt. of time for which it was done in mins:",habit[2])

print("\nDay 1:", record[0])
print("Day 7:", record[6])
 
ffd = record[0:4]
print("First five days:", ffd)
 
wed = record[5:7]
print("Weekend days:", wed)

weekly_record = record + (0,)
print("Adding the record for the 8th day:", weekly_record)
 
comp = weekly_record.count(1)
not_comp = weekly_record.count(0)
 
print("\nCompleted days:", comp)
print("Not completed days:", not_comp)
 
d = 0
nd = 0
 
for i in range(len(weekly_record)):
    if weekly_record[i] == 1:
        d += 1
    else:
        nd += 1
if d > nd:
    print("\nYou were great!! \nAmazing:)")
else:
    print("\nYou missed a lot of days:(")