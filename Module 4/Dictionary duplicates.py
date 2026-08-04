student_data = {'id1':
    {'name':['Sara'],
     'class':['V'],
     'sub_int':['Eng,science,Maths']
    },
    'id2':
    {'name':['david'],
     'class':['V'],
     'sub_int':['Eng,science,Maths']
    },
    'id3':
    {'name':['Sara'],
     'class':['V'],
     'sub_int':['Eng,science,Maths']
    },
    'id4':
    {'name':['John'],
     'class':['V'],
     'sub_int':['Eng,science,Maths']
    }
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
    else:
        print(key,"is already present!!")

print(result)