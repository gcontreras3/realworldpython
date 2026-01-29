# Looping through an Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    # For every magician in the list, print their name
    print(f"{magician.title()}, that was a great trick!")
    if magician == 'david':
        print(f'{magician.title()}, you are the best magician!')
print("Thank you, everyone. That was a great magic show!")


# Using the range() Function
# This function prints out the numbers 1 - 10 but because the end value is set to 10, when the program reaches the end value it stops and does not include it in the output.
for value in range(1, 10):
    print(value)

# Creating a List of Numbers
numbers = list(range(20, 41))
print(numbers)
even_numbers = list(range(2, 21, 2))
print(even_numbers)
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

# more concise way to write the above code
squares2 = []
for value in range(1, 5):
    squares2.append(value ** 2)
print(squares2)

"""
Sometimes using a temporary variable makes your code eas-
ier to read; other times it makes the code unnecessarily long. Focus first on
writing code that you understand clearly, which does what you want it to do.
Then look for more efficient approaches as you review your code.

"""

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("New list of digits:", digits)
min(digits)
max(digits)
sum(digits)


# list comprehensions
squares3 = [value ** 2 for value in range(1, 11)]
print(squares3)
"""
To use this syntax, begin with a descriptive name for the list, such as
squares. Next, open a set of square brackets and define the expression for
the values you want to store in the new list. In this example the expres-
sion is value**2, which raises the value to the second power. Then, write
a for loop to generate the numbers you want to feed into the expression,
and close the square brackets. The for loop in this example is for value
in range(1, 11), which feeds the values 1 through 10 into the expression
value**2. Notice that no colon is used at the end of the for statement.

"""

# Slicing a list
# To make a slice, you specify the index of the first and last elements you want to work with.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Quick tip
"""
Anytime you want to start from the beginning of a list, and go to the end, you can leave the stop blank."""
players[2:] # from the 3rd element to the end
players[:] # the whole list (copy)