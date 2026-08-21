import random

def generate_password():
    password_list = [
        chr(random.randint(65, 90)),   
        chr(random.randint(97, 122)),  
        chr(random.randint(48, 57)),   
        chr(random.randint(33, 47))   
    ]
    all_ascii_codes = (
        list(range(65, 91)) + 
        list(range(97, 123)) +  
        list(range(33, 58))     
    )
    for i in range(4):
        random_code = random.choice(all_ascii_codes)
        password_list.append(chr(random_code))
    random.shuffle(password_list)
    password_string = ""
    for character in password_list:
        password_string += character

    return password_string

secure_password = generate_password()
print(f"Generated Password: {secure_password}")
