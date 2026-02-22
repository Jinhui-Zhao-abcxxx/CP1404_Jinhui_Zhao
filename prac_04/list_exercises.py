
user_numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input('Enter username: ')
if username in usernames:
    print("Access granted")
    for i in range(5):

        number = int(input("Enter a number: "))
        user_numbers.append(number)
    print(f"The first number is {user_numbers[0]}")
    print(f"The last number is {user_numbers[-1]}")
    print(f"The smallest number is {min(user_numbers)}")
    print(f"The largest number is {max(user_numbers)}")
    print(f"The average number is {sum(user_numbers)/len(user_numbers)}")

else:
    print("Access denied")