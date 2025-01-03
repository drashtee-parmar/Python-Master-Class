# A palidrom is a word that reads the same backwords as forwards.
# Palidromes are normally created for fun. There's nothing wring with having a bit of fun, but

# def is_palindrome(string):
def is_palindrome(string: str) -> bool: # annotations
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """

    # backwards = string[::-1] # reverse the original string
    # return backwards == string
    return string[::-1].casefold() == string.casefold()  # casefold for upper and lower case strings


# word = input("please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


# racecar = Palidrome
# python = not palindrome

#
# Create a new function called palidrome_sentence
# The function should return True if the sentence is a palindrome - False, otherwise.
# Remember that we ignore spaces, punctuation and things like tabs and line feeds. We're only interested in alphanumeric characters.
#

# def palindrome_sentence(sentence):
def palindrome_sentence(sentence: str) -> bool:
    """
        Check if a sentence is a palindrome.

        The function ignores whitespace, capitalisation and
        punctuation in the sentence.

        :param sentence: The sentence to check.
        :return: True if `sentence` is a palindrome, False otherwise.
        """

    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()  # casefold for upper and lower case strings
    return is_palindrome(string)

# word = input("please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# Was it a car, or a cat, I saw = Palidrome.
# Radar = Palidrome.
# do geese see god? = Palidrome.


# p = is_palindrome()
