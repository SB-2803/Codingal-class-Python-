snack_box1 = {"chips", "momos", "cookies", "chips", "noodles"}
snack_box2 = {"cookies", "sandwich", "juice", "sandwich"}
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
snack_box1.add("banana")
print("Snack Box 1 after adding banana:", snack_box1)
common = snack_box1.intersection(snack_box2)
print("Snacks present in both boxes:", common)
import array as a
snack_counts = a.array('i', [4, 6, 3, 5])
print("Snack counts array:", snack_counts)
snack_counts.insert(3, 8)
snack_counts.append(9)
print("Snack counts after adding items:", snack_counts)
count_of_4 = snack_counts.count(4)
print("Number of times 4 appears:", count_of_4)
snack_counts.reverse()
print("Reversed snack counts array:", snack_counts)

