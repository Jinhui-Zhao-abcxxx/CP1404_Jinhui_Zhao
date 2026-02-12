MENU =  "(H)ello\n(G)oodbye\n(Q)uit\n"

def show_menu():
    print (MENU)
    print (">>>",end="" )

def main():
    user_name = input("Enter your name: ")
    show_menu()
    user_choice = input(" ").upper()
    while user_choice != "Q":
        if user_choice == "H":
            print(f"Hello {user_name}")
        elif user_choice == "G":
            print(f"Goodbye {user_name}")
        else:
            print("Invalid choice")
        show_menu()
        user_choice = input(" ").upper()
    print("Finished.")



main()

