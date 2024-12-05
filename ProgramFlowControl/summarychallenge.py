# choice = "_"
# while choice != "0":
#     if choice in "12345":
#         print("You choose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")
#     choice = input()


choice = None

while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        break

    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")
