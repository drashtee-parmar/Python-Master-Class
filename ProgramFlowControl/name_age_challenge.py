# Write a small program to ask for a name and an age.

# When both values have been enter, check if the person is the right age to go on an 18-30 holiday
# (they must be 18 and under 31)

# if they are, welcome them to the holiday, otherwise print a (polite)
# message refusing them entry.

name = input("What is your name? ")
age = int(input("What is your age? "))

# if (age  >= 18) and (age <= 30):
if (18 <= age < 31):
    print("Welcome to the club 18-30  holiday, {}".format(name))
else:
    print("Sorry, Our holiday are only for cool people. Better luck next time!")
