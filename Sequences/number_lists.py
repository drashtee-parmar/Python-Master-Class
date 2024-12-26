# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# print("min even number in the list")
# print(min(even))
# print("*" * 30)
# print()
#
# print("Max even number in the list")
# print(max(even))
# print("*" * 30)
# print()
#
# print("Max odd number in the list")
# print(min(odd))
# print("*" * 30)
# print()
#
# print("Max odd number in the list")
# print(max(odd))
# print("*" * 30)
# print()

# print()
# print(len(even))
# print(len(odd))
#
# #count how many times it appears in a string
# print()
# # print("mississippi".count("s"))
# print("mississippi".count("issi"))

# --------------------------------------------------------
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# # Extend method takes all we pass it to the lists
# print("Print by combining together")
# even.extend(odd) # it passes from odd to even
# print(even)
# another_even = even
# print(another_even)
#
# print("Rearrange in sorted order")
# even.sort()
# print(even)
#
# print("Rearrange in reverse order")
# even.sort(reverse=True)
# print(even)
# print(another_even)


# ------------------------------------------------
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# numbers = even + odd
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)


# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# # digits = sorted("432985617")
# digits = list("432985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]# slicing
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers) # not the same list...
# print(numbers == more_numbers)
