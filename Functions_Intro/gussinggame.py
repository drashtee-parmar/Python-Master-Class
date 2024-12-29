import random


def get_integer(prompt):
    """
    Get the integer from standard input(stdin).
    the function will continue looping and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user will see, when
        they're prompted to enter the value
    :return: the integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        #     print("{0} is not a valid number". format(temp))
        print("{0} is not a valid number".format(temp))

help(get_integer)
# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
print(answer)
guess = 0  # initialise to any number that does not equal to answer
print("Please guess the number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
