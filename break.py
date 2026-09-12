print("What do you wish to do ?")
print("1) Pick an activity")
print("2) add an activity")

import json
import random

choice = int(input())

if (choice == 1):
    print("Filter by: ")
    print("Screen-based? (y/n)")
    screen = True if input() == "y" else False

    print("Educational? (y/n)")
    edu = True if input() == "y" else False
    try:
        with open("data.json", "r") as f:
            activities = json.load(f)
    except FileNotFoundError:
        activities = []
    
    filtered = []
    for a in activities:
        if a["screen"] == screen and a["educational"] == edu:
            filtered.append(a)
    if len(filtered) == 0:
        print("No activities match your criteria")
        exit()
    pick = random.choice(filtered)
    print(pick["name"])
else:
    print("Screen-based? (y/n)")
    screen = True if input() == "y" else False

    print("Educational? (y/n)")
    edu = True if input() == "y" else False

    print("Activity name? ")
    name = input()

    if not name:
        print("Empty names not allowed.")
        exit()

    new = {"name": name, "screen": screen, "educational": edu}

    try:
        with open("data.json", "r") as f:
            activities = json.load(f)
    except FileNotFoundError:
        activities = []
    
    activities.append(new)
    with open("data.json", "w") as f:
        json.dump(activities, f, indent = 4)

