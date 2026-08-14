#Phonebook dictionary (name->number)
phonebook = {
    'Sara': '9876543100',
    'David':'9768543210',
    'John':'8910887766'
}

#search a contact safely
name = input("Enter a name to get his/her contact:")
print("Number:",phonebook.get(name,'Not found'))

#delete a contact only if it exists
del_name = input("Enter a name to delete his/her number:")

if del_name in phonebook:
    del phonebook[del_name]
    print(del_name,"Deleted Permanently!!")
else:
    print("Cannot delete. Not found")

#Print updated notebook
print("\nUpdated phonebook:",phonebook)

#Adding a number
name = input("Enter a name to add his/her number:")
no = input("Enter his/her number:")
phonebook[name]=no

#Print updated notebook
print("\nUpdated phonebook:",phonebook)