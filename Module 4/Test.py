student_grade_book={'Alice':90,
                    'John':99,
                    'Siddhi':89,
                    'Rahul':78,
                    'Uraa':65
                    }
print("The student grade book of class 8 is(note all marks are out of 100):",student_grade_book)
highest = max(student_grade_book.values())
for key,values in student_grade_book.items():
    if values == highest:
        print("The highest scorer is:",key)
lowest = min(student_grade_book.values())
for key,values in student_grade_book.items():
    if values == lowest:
        print("The lowest scorer is:",key)
sum1 = 0
for values in student_grade_book.values():
    sum1+=values
    avg = sum1/len(student_grade_book)
print("The average of the class is:",avg)
choice = input("Enter the student whose marks you want to see:")
print("Marks of",choice,"is",student_grade_book.get(choice,'Not found:('))
