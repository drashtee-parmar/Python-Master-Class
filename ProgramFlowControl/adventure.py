available_exits = ["north", "south", "east", "west"]

chosen_exits = ""
while chosen_exits not in available_exits:
    chosen_exits = input("please choose a direction: ")
    if chosen_exits.casefold() == "quit":
        print("Game over!")
        break

else:
    print("Aren't you glad you got our to there?")
