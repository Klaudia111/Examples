import random
print("Create password 4 letters only lowercase")
password=input("Password: ")
if len(password) == 4:
    pass
else:
    print("Password is invalid")
    exit(0)

letters = 'abcdefghijklmnoprstuwxyz'
try_password = ''

while True:
    for i in range(4):
        print(i)
        letter = random.choice(letters)
        try_password += letter
        print(try_password)
    if try_password == password:
        print("Your password was found :", try_password)
        break
    else:
        try_password=''

