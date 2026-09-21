
def main():
    file_names = []
    user_input = input("input your file name:")
    file_names.append(user_input)
    while user_input != "":
        is_finished = False
        while not is_finished:
            try:
                file = open(user_input,"r")
            except FileNotFoundError:
                print("Error: file not found")
                user_input = input("input your file name:")
            else:
                file_contents = file.readlines()
                print(f"{user_input} has {len(file_contents)} lines")
                is_finished = True

        user_input = input("input your file name")



main()


