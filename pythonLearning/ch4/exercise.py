# Exercise 4-1: Pizzas
"""store the names of a few pizzas in a list, then use a for loop to print the name of each pizza."""
pizzas = ['New York Style', 'Chicago Style', 'Pepperoni', 'Cheese']

for x in pizzas:
    y = 1
    print(f'{y}. I like {x} pizza.')
    y = y + 1
print('I really love pizza!')

for i, pizza in enumerate(pizzas, start=1):
    print(f'{i}. I like {pizza} pizza.')
print('This is the second list using enumerate function.')

# Exercise 4-2: Animals
"""store the names of a few animals in a list, then use a for loop to print the name of each animal."""
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(animal)
    print(f'A {animal} would make a great pet.')


# 4-3: Counting to Twenty
"""use a for loop to print the numbers from 1 to 20, inclusive."""
for number in range(1, 21):
    print(number)

"""million_numbers = list(range(1, 100_000_001))
for x in million_numbers:
    print(min(million_numbers))
    print(max(million_numbers))
    print(sum(million_numbers)) """

# Exercise 4-6: Odd Numbers

odd_numbers = list(range(1, 21, 2))
print(f'odd_numbers list: {odd_numbers}')

# Exercise 4-7: Threes
threes = []
for value in range(3, 31, 3):
    threes.append(value)
print(f'threes list: {threes}')

# Exercise 4-8: Cubes
cubed = []
for value in range(1, 11):
    cubed.append(value ** 3)
print(f'cubed list: {cubed}')


# Exercise 4-9: Cube Comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(f'cubes list using list comprehension: {cubes}')

