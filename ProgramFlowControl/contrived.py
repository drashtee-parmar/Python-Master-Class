# numbers = [1, 45, 32, 12, 60]
# numbers = [1, 45, 31, 12, 60]
numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # Reject the list
        print("The numbers are unacceptable.")
        break
    else:
        print("All those numbers are fine.")
