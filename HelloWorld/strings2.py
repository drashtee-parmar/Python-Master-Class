#         01234567890123
parrot = "Norwegian Blue"

# ----------------- Part 5 -----------------------
# Slicking Backwards



# ----------------- Part 4 -----------------------
# Using step in a slice : Start, stop, step
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4] #slicking every 4th character
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

# ----------------- Part 3 -----------------------

# print(parrot[0:6])  # Norweg
# print(parrot[-14:-8])  # Norweg
# print(parrot[-4:-2])  # Bl
# print(parrot[-4:12])  # Bl

# ----------------- Part 2 -----------------------

# Slicing : up to but not including -> Start Stop Values
# print(parrot[0:6]) #Norweg
# print(parrot[3:5]) # we
# print(parrot[0:9]) #Norwegian
# print(parrot[:9]) #Norwegian
# print(parrot[10:14]) #Blue
# print(parrot[10:]) #Blue
#
# print(parrot[:6]) #Norweg
# print(parrot[6:]) #ian Blue
#
# print(parrot[:6] + parrot[6:])
# print(parrot[:]) #Norwegian Blue


# ----------------- Part 1 -----------------------
# print(parrot)
# print("Positive indexing: " )
# print((parrot[3]))
# print((parrot[4]))
# print((parrot[9]))
# print((parrot[3]))
# print((parrot[6]))
# print((parrot[8]))
#
#
# print()
# print("Negative indexing for Norwegian Blue")
# # print((parrot[-1])) # last character
# # print((parrot[-14])) # it goes backward to forward
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
#
# print()
# print((parrot[3 - 14]))
# print((parrot[4 - 14]))
# print((parrot[9 - 14]))
# print((parrot[3 - 14]))
# print((parrot[6 - 14]))
# print((parrot[8 - 14]))
