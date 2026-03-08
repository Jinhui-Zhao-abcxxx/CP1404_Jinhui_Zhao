"""
CP1404/CP5632 Assignment 1 – Travel Tracker 1.0
Jinhui.Zhao
"""
import random
from operator import itemgetter

MENU = "Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit "



def main():
    print("Travel Tracker 1.0 - by Jinhui.Zhao")

    original_places = read_csv()

    # print(original_places)
    # this is used for testing

    visited_places,unvisited_places = clean_data(original_places)

    # print(visited_places)
    # print(unvisited_places)
    # this is used for testing

    print(f"{len(original_places)} places loaded from places.csv")

    show_menu()

    user_input = input(">>>".lower())
    while user_input != "q":

        if user_input == "d":

            display_all_places(unvisited_places, visited_places)

            show_menu()
            user_input = input(">>>".lower())

        elif user_input == "r":

            if len(unvisited_places) == 0:
                print("No places left to visit!")

            else:
                random_number = random.randint(0,len(unvisited_places) - 1)
                print("Not sure where to visit next?")
                print(f"How about...  {unvisited_places[random_number][0]:>{len(unvisited_places[random_number][0])}} in {unvisited_places[random_number][1]:>{len(unvisited_places[random_number][1])}}?")

            show_menu()
            user_input = input(">>>".lower())

        elif user_input == "a":

            new_place = []



            new_name = check_blank("Name:")
            new_country = check_blank("Country:")
            new_priority = check_if_valid("priority:")
            new_place.append(new_name)
            new_place.append(new_country)
            new_place.append(new_priority)

            # print(new_place)
            # this is used for testing

            unvisited_places.append(new_place)
            sort_places(unvisited_places)

            show_menu()
            user_input = input(">>>".lower())

        elif user_input == "m":
            display_all_places(unvisited_places, visited_places)

            print("Enter the number of a place to mark as visited")
            mark_number = check_if_valid(">>>")
            if mark_number > len(unvisited_places):
                print(f"You have already visited {visited_places[mark_number - len(unvisited_places)]}")
            else:
                print(f"{unvisited_places[mark_number][0]:>{len(unvisited_places[mark_number][0])}} in {unvisited_places[mark_number][1]:>{len(unvisited_places[mark_number][1])}} visited! ")
                unvisited_places[mark_number] = unvisited_places[mark_number][:-1] + "v"
                visited_places.append(unvisited_places[mark_number])
                unvisited_places.pop(unvisited_places[mark_number])
                sort_places(unvisited_places)

            show_menu()
            user_input = input(">>>".lower())

        else:
            print("Invalid menu choice")

    new_file = open("places.csv","w")
    write_file(new_file, unvisited_places)
    write_file(new_file, visited_places)
    new_file.close()
    print(f"{len(unvisited_places) + len(visited_places)} places saved to places.csv ")
    print("Have a nice day :)")


def write_file(new_file, list_of_places):
    for place in list_of_places:
        for place_info in place:
            print(place_info, end=",", file=new_file)
        print("",file=new_file)


def display_all_places(unvisited_places, visited_places):
    max_length_country, max_length_name = get_display_length(unvisited_places, visited_places)

    # print(max_length_name)
    # print(max_length_country)
    # this is used for testing

    display_places(max_length_country, max_length_name, unvisited_places, visited_places)

    print(f"{len(visited_places) + len(unvisited_places)} places tracked. You still want to visit {len(unvisited_places)} places.")

def get_display_length(unvisited_places, visited_places):
    max_length_name = max(get_max_length(0, visited_places), get_max_length(0, unvisited_places))
    max_length_country = max(get_max_length(1, visited_places), get_max_length(1, unvisited_places))
    return max_length_country, max_length_name


def check_if_valid(promo):
    is_pass = False

    while not is_pass:
        try:
            new_thing = int(input(promo))

            if new_thing <= 0:
                print("Number must be > 0")
            else:
                is_pass = True
        except ValueError:
            print("Invalid input; enter a valid number")

    return new_thing


def check_blank(promo):
    new_thing = input(promo)
    while new_thing == "":
        print("Input can not be blank")
        new_thing = input(promo)
    return new_thing


def display_places(max_length_country, max_length_name,unvisited_places,visited_places,):

    display_number = 0

    for place in unvisited_places:
        display_number += 1
        print(f"*{display_number}. {place[0]:<{max_length_name}} in {place[1]:<{max_length_country}} {place[2]}")

    for place in visited_places:
        display_number += 1
        print(f"{display_number}. {place[0]:<{max_length_name}} in {place[1]:<{max_length_country}} {place[2]}")



def clean_data(original_places):
    visited_places = []
    unvisited_places = []
    for place_info in original_places:
        if place_info[-2] == "n":
            unvisited_places.append(place_info[:-1].split(","))
        else:
            visited_places.append(place_info[:-1].split(","))

    sort_places(unvisited_places)

    return visited_places,unvisited_places


def sort_places(unvisited_places):
    unvisited_places.sort(key=itemgetter(2))
    unvisited_places.reverse()


def read_csv():
    places_file = open("places.csv", "r")
    original_places = places_file.readlines()
    places_file.close()
    return original_places


def show_menu():
    print(MENU)

def get_max_length(position,places_list):
    measuring_list = []
    for place in places_list:
        measuring_list.append(place[position])
    return len(max(measuring_list))





main()