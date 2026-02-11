# 1.
def question_1():
    namefile = open("name.txt","a")
    name = input("Enter your name: ")
    print(f"{name}\t",file=namefile)
    namefile.close()

# 2.
def question_2():
    namefile = open("name.txt","r")
    names = namefile.readlines()
    for name in names:
        print(f"Hi {name.strip()}!")
    namefile.close()

# 3.
def rewrite_numbers():
    number_file = open("numbers.txt","w")
    numbers = [17,42,400]
    for number in numbers:
        print(f"{number}\t",file=number_file)
    number_file.close()

def question_3():
    with open("numbers.txt","r") as number_file:
        numbers = number_file.readlines()
        total = int(numbers[0]) + int(numbers[1])
        print(f"Total: {total}")


# 4.
def question_4():
    with open("numbers.txt","r") as number_file:
        numbers = number_file.readlines()
        total_number = 0
        for number in numbers:
            total_number += int(number)
        print(f"Total: {total_number}")


question_3()
question_4()
question_2()