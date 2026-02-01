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



# Exercise 3-4: Guest List
""" If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner, and then print a message to each person, inviting them to dinner.
"""

guest_list = ['Albert Einstein', 'Napoleon Bonaparte', 'Cleopatra', 'Marcus Aurelius', 'Louis', 'Jake', 'Adam']

print(f'Dear {guest_list[0]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[1]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[2]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[3]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[4]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[5]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[6]}, I would be honored if you could join me for dinner.')
print("\n")
# Exercise 3-5: Changing Guest List
""" You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. 
You'll have to think of someone else to invite. 

Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.

"""

print(f'Unfortunately, {guest_list[2]} cannot make it to the dinner.\n')
guest_list[2] = 'Marie Curie'

print(f'Dear {guest_list[0]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[1]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[2]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[3]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[4]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[5]}, I would be honored if you could join me for dinner.')
print(f'Dear {guest_list[6]}, I would be honored if you could join me for dinner.')
print("\n")

# Exercise 3-6: More Guests
""" You just found a bigger dinner table, so now more space is available.
Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
print("Good news! I found a bigger dinner table, so more guests can join us.\n")
guest_list.insert(0, 'Socrates')
guest_list.insert(4, 'Leonardo da Vinci')
guest_list.append('Isaac Newton')

# Exercise 3-7: Shrinking Guest List
""" You just found out that your new dinner table won’t arrive in time for
dinner, and you have space for only two guests.
Start with your program from Exercise 3-6. Add a new line that prints a message
saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
guests remain. Each time you pop a name from your list, print a message to that person
letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program. """

print("Unfortunately, I can invite only two people for dinner.\n")

guest_list.pop()
print(f'Dear {guest_list.pop()}, I am sorry I cannot invite you to dinner.\n')
print(f'Dear {guest_list.pop()}, I am sorry I cannot invite you to dinner.\n')
print(f'Dear {guest_list.pop()}, I am sorry I cannot invite you to dinner.\n')
print(f'Dear {guest_list.pop()}, I am sorry I cannot invite you to dinner.\n')
print(f'Dear {guest_list[0]}, you are still invited to dinner.\n')
print(f'Dear {guest_list[1]}, you are still invited to dinner.\n')

# Exercise 3-8: Seeing the World
""" Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order.
• Print your list in alphabetical order by using sorted().
• Show that your list is still in its original order by printing it again.
• Print your list in reverse alphabetical order by using sorted() with reverse=True.
• Show that your list is still in its original order by printing it again.
• Change the order of your list by using reverse().
• Print your list to show that its order has changed.
• Change the order of your list again by using reverse().
• Print your list to show that it’s back to its original order.
• Sort your list alphabetically by using sort().
• Print your list to show that it’s now sorted alphabetically.
• Sort the list in reverse alphabetical order by using sort() with reverse=True.
• Print your list to show that it’s now sorted in reverse alphabetical order. """

places = ['Vietnam', 'Mexico', 'Italy', 'Spain', 'London']
print(f'Original list: {places}')
print(f'Alphabetically sorted: {sorted(places)}')
print(f'Original list: {places}')
print(f'Reverse alphabetically sorted: {sorted(places, reverse=True)}')
print(f'Original list: {places}')
places.reverse()
print(f'Reversed list: {places}')
places.reverse()
print(f'Back to original order: {places}')
print(f'The number of people on the guest list is: {len(guest_list)}')
print(f'The number of places I want to visit is: {len(places)}')

