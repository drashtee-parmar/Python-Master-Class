# -1 for slicking is for reversing items
letters = "abcdefghijklmnopqrstuvwxyz"
# letters = " "

# backwards = letters[25:0:-1] # it will not have a included
# backwards = letters[25::-1] # it will not have a included
# backwards = letters[::-1] # it will not have a included
# print(backwards)

# Create a slice that produces the characters qpo
backwards = letters[16:13:-1]
print(backwards)
# Slice the string to produce edcba
print(letters[4::-1])
# Slice the string to produce the last 8 character in reverse order
print(letters[:-9:-1])

print(letters[-4:])#last 4

print(letters[-1:]) # last character

print(letters[:1])
print(letters[0])
