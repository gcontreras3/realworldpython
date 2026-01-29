

print(f'I would like to own a {transportation_modes[-1].title()} one day.')
print(f'My favorite mode of transportation is the {transportation_modes[3].title()}.')


# Modify an element in a list
# Modifying the first element of the cars list
cars = ['Tesla', 'BMW', 'Audi', 'Mercedes', 'Ford']
cars[0] = 'Porsche'
print(cars)

# Adding elements to a list
# Appending an element to the end of the list

cars.append('Chevrolet')
print(cars)

# Inserting an element at a specific position
cars.insert(2, 'Honda')
print(cars)


# Creating an empty list and adding elements to it
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


# inserting elements at specific positions
motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removing elements from a list
# Using the del statement to remove an element by its index

del motorcycles[1]
print(motorcycles)

# Using the pop() method to remove the last element and store it in a variable
""" The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack.
The pop() method removes the last item in a list, but it lets you work with that item after removing it.
"""
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

# Popping an item from a specific position
first_motorcycle = motorcycles.pop(0)
print(first_motorcycle)
print(motorcycles)

print(f"The first motorcycle I owned was a {popped_motorcycle.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# The remove() method deletes only the first occurrence of the value you specify
# Chapter 7 Loops