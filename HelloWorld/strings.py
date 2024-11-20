print("Today is a good day to learn python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")  # String concatenation
greeting = "Hello"
name = "Dona"
# name = input("Please enter your name: ")
# if we want space we can add that too
print(greeting + name)
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")  # putting f befor quote
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
