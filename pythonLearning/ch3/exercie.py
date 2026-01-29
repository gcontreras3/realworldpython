# Exercise 3-1: Names
# Store the names of a few of your friends in a list called friends.

friends = ['John', 'Jake', 'Louis', 'Tracy', 'Aldjia', 'Fadila']
# Exercise 3-2: Greetings
for friend in friends:
    message = f'Hello, {friend.title()}! How are you doing today?'
    print(message)
    print("\n")  # Print a newline for better readability between friends' messages

print("Thank you all for being such great friends!")

# Exercise 3-3: Your Own List
# A list is a collection of items in a paricular order. Lists are mutable, meaning their contents can be changed after they are created.
# Lists are ordered collections, access any element by its index.

family = ['Jerry', 'Ivan', 'mom', 'dad', 'brother', 'sister', 'dog']

print(family[3].title())
print(family[-1].upper())

message = f'My family member is {family[1].title()}, and he is great!'
print(message)

# Favorite mode of transportation
transportation_modes = ['car', 'bike', 'bus', 'train', 'airplane', 'scooter', 'boat', 'motorcycle']
# Create a list of your favorite foods and print each food item.