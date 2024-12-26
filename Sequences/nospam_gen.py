menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
# write code to print out all the meal in the menu, but with spam removed.
# you can choose which approach you want to use:
#     - Remove spam from each list, then print the list
#     - Print out the items in each list, as long as its not spam.
# you may want to write two sets of code, using both approach

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))


# using generator method
# for meal in menu:
#     items = ", ".join((item for item in meal if item != "spam"))
#     print(items)
