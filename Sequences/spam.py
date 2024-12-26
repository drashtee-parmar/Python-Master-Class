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
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)

for index, meal in enumerate(menu):
    if "spam" not in meal:
        print (index, meal)
        # using nested for condition
        for item in meal:
            print(item)
    else:
        print("{0} has a span of {1}"
              .format(meal, meal.count("spam")))
