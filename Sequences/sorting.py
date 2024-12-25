pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.6, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers) # it works using variable
print(sorted_numbers)

print(numbers)

# another_sorted_numbers = numbers.sort() # it will show None as cant assign sort() to the variables
numbers.sort()
print(numbers)
# print(another_sorted_numbers)


missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)# dont include paranthesis for casefold, case insensitive
print(missing_letter)


names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)
