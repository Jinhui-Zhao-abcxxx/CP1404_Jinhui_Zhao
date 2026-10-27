"""
CP1404 Prac_7
Project Management Program by Jinhui Zhao
time estimate: 1 hour
"""
import datetime

from project import Project

def show_menu():
    print("- (L)oad projects \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit")

def check_empty(prompt):
    user_input = input(prompt)
    while user_input == "":
        print("enter something")
        user_input = input(prompt)
    return user_input

def load_file(filename) :
    in_file = open(filename, "r")
    in_file.readline()
    projects = []
    for line in in_file:
        project = line.strip().split()
        is_pass = False
        while not is_pass:
            try:
                datetime.datetime.strptime(project[1],"%d/%m/%Y")
            except ValueError:
                project[0] += " " + project[1]
                project.pop(1)

            else:
                is_pass = True
        projects.append(Project(project[0], datetime.datetime.strptime(project[1], "%d/%m/%Y").date(), int(project[2]),
                                float(project[3]), float(project[4])))
    in_file.close()
    return projects

def save_file(projects):
    saving_file = check_empty("Enter the file name you want to save")
    in_file = open(saving_file, "w")
    for project in projects:
        print(project, file=in_file)
        in_file.close()
def check_integer(prompt):
    integer_input = input(prompt)
    is_pass = False
    while not is_pass:
        try:
            int(integer_input)
        except ValueError:
            print("please enter a number")
            integer_input = check_empty("Priority:")
        else:
            is_pass = True
    return integer_input

def check_time_valid(prompt) :
    time_input = input(prompt)
    is_pass = False
    while not is_pass:
        try:
            datetime.datetime.strptime(time_input, "%d/%m/%Y")
        except ValueError:
            print("enter a valid time")
            time_input = input(prompt)
        else:
            time_input = datetime.datetime.strptime(time_input, "%d/%m/%Y").date()
            is_pass = True
    return time_input

def check_float(prompt):
    float_input = check_empty(prompt)
    is_pass = False
    while not is_pass:
        try:
            float(float_input)
        except ValueError:
            print("enter a valid value")
            float_input = check_empty(prompt)
        else:
            is_pass = True
    return float_input

def main():

    projects = load_file("projects.txt")
    completed_projects = []
    incomplete_projects = []

    for project in projects:
        if project.is_completed():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)

    completed_projects.sort()
    incomplete_projects.sort()

    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from projects.txt")
    show_menu()
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            new_file = check_empty("Enter new file name")
            is_pass = False
            while not is_pass:
                try:
                    load_file(new_file)
                except FileNotFoundError:
                    print("File not found")
                    new_file = check_empty("Enter new file name")
                else:
                    is_pass = True
            projects = load_file(new_file)
            print(f"Loaded {len(projects)} projects from {new_file}")

            user_input = input(">>> ").upper()
            show_menu()

        elif user_input == "S":
            save_file(projects)

            user_input = input(">>> ").upper()
            show_menu()

        elif user_input == "D":
            print("incomplete projects:")
            for project in incomplete_projects:
                project.show_project_info()
            print("Completed projects:")
            for project in completed_projects:
                project.show_project_info()

            user_input = input(">>> ").upper()
            show_menu()

        elif user_input == "F":
            time_input = check_time_valid("Show projects that start after date (dd/mm/yy):")
            for project in projects:
                if project.start_date > time_input:
                    project.show_project_info()

            user_input = input(">>> ").upper()
            show_menu()

        elif user_input == "A":
            print("Let's add a new project")
            new_name = check_empty("name:")
            new_time = check_time_valid("Start date (dd/mm/yy): ")
            new_priority = check_integer("Priority:")
            new_cost = check_float("Cost estimate: $")
            new_percentage = check_float("Percent completed:")

            new_project = Project(new_name,new_time,new_priority,new_cost,new_percentage)
            projects.append(new_project)
            if new_project.percent == 100:
                completed_projects.append(new_project)
            else:
                incomplete_projects.append(new_project)

            completed_projects.sort()
            incomplete_projects.sort()

            user_input = input(">>> ").upper()
            show_menu()

        elif user_input == "U":
            project_count = 0
            for project in projects:
                project_count += 1
                print(project_count,end=" ")
                project.show_project_info()

            user_choice = int(check_integer("Project choice:"))

            while user_choice <= 0 or user_choice >= project_count:
                print("enter a valid number")
                user_choice = int(check_integer("Project choice:"))

            projects[user_choice- 1].show_project_info()

            new_percent = check_float("New Percentage:")
            projects[user_choice - 1].percent = new_percent
            new_priority = input("New Priority:")
            is_pass = False
            while new_priority != "" and not is_pass:
                try:
                    int(new_priority)
                except ValueError:
                    print("enter a number")
                    new_priority = input("New Priority:")
                else:
                    is_pass = True
                    new_priority = int(new_priority)
            projects[user_choice - 1].priority = new_priority

            user_input = input(">>> ").upper()
            show_menu()

        else:
            print("invalid choice")

            user_input = input(">>> ").upper()
            show_menu()

    user_save_choice = input("Would you like to save to projects.txt?").upper()
    if user_save_choice == "Y":
        save_file(projects)
    print("Thank you for using custom-built project management software.")


main()


