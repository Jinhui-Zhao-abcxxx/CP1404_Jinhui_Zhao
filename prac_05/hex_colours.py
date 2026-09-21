COLOURS_NAMES = {"absolute zero": "#0048ba", "acid green": "#b0bf1a","aliceblue": "#f0f8ff",
                 "aqua": "#00ffff","aquamarine1":  "#7fffd4","aquamarine2": "# 76eec6","aquamarine4": "# 458b74",
                 "amber" : "#ffbf00","amethyst": "#9966cc" }


search_colour = input("Enter colour: ").lower()

while search_colour !="":
    try:
        print(COLOURS_NAMES[search_colour])
        search_colour = input("Enter colour: ").lower()
    except KeyError:
        print("Invalid colour")
        search_colour = input("Enter colour: ").lower()




