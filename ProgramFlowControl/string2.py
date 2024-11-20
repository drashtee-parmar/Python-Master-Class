
# number = "9,223;372:036 854,775;807"
number = input("Please enter a sereis of numbers, using any seperators you like: ")

# seperators = number[1::4] #slicking every 4th character
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
# print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))

# --------------------- Reference: -------------------------
# https://docs.python.org/3/library/functions.html
