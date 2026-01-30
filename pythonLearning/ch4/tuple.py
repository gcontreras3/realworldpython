# Tuples are a list of items that cannot be changed
# Tuples are immutable

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
# Tuples can contain different data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)
# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)
# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print("Nested tuple:", nested_tuple)
# Length of a tuple
print("Length of my_tuple:", len(my_tuple))
# Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# You can assign a new value to a variable that represents a tuple

my_tuple = (10, 20, 30)
print("New tuple assigned to my_tuple:", my_tuple)