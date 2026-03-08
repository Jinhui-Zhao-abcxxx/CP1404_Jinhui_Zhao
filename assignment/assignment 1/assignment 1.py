"""
CP1404/CP5632 Assignment 1 – Travel Tracker 1.0
Jinhui.Zhao
"""
import random
MENU = "Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit "



def main():
    print("Travel Tracker 1.0 - by Jinhui.Zhao")
    original_places = read_csv()
    # print(original_places)    """this is used for testing"""
    cleaned_places = clean_data(original_places)
    # print(cleaned_places)    """this is used for testing"""
    print(f"{len(cleaned_places)} places loaded from places.csv")
    show_menu()


def clean_data(original_places):
    cleaned_places = []
    for place_info in original_places:
        cleaned_places.append(place_info[:-3].split(","))
    return cleaned_places

def read_csv():
    places_file = open("places.csv", "r")
    original_places = places_file.readlines()
    places_file.close()
    return original_places


def show_menu():
    print(MENU)



main()