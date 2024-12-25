computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball"
# print(computer_parts)

# using slice
print(computer_parts[3:]) # Slicing

computer_parts[3:] = "trackball" # Assigning to a variable will work differently with quotation and have string saperated
print(computer_parts)
computer_parts[3:] = ["trackball"] #
print(computer_parts)



#
# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])  # index position of computer part
#
# # Slice list
# print("*" * 50)
# print(computer_parts[0:3])
# print(computer_parts[-1])
