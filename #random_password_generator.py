#random_password_generator_python
import random
import string

letters_lc=string.ascii_lowercase
letters_uc=string.ascii_uppercase
digits=string.digits
special=string.punctuation

pwd= [''] 
pwd.extend(letters_lc) 
pwd.extend(letters_uc) 
pwd.extend(digits) 
pwd.extend(special)

pwdlen=int(input('Enter Password Length: '))

if pwdlen<=7:
    print("Please Try again by entering number atleast greater than 8 ")

else:
    random.shuffle(pwd)
    output=""
    print(output.join(pwd[0:pwdlen]))