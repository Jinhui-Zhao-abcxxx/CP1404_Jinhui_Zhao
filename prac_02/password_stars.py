LENGTH_OF_PASSWORD = 8



def main():
    password = validate_password_length()
    for i in range(len(password)):
        print("*",end="")

def validate_password_length():
    password = str(input('Enter a password: '))
    while len(password) < LENGTH_OF_PASSWORD:
        print("Password must be at least 8 characters long")
        password = str(input('Enter a password: '))
    return password

main()


