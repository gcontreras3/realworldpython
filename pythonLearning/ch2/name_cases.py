jerry = "Jerry"
print(jerry.lower()) # Output: jerry
print(jerry.upper()) # Output: JERRY
print(jerry.title()) # Output: Jerry
print(jerry.capitalize()) # Output: Jerry
print(jerry.swapcase()) # Output: jERRY
print(jerry.replace('J', 'K')) # Output: kerry
print(jerry.center(20)) # Output: '       Jerry        '
print(jerry.ljust(20)) # Output: 'Jerry               '
print(jerry.rjust(20)) # Output: '               Jerry'
print(jerry.count('r')) # Output: 2
print(jerry.startswith('J')) # Output: True
print(jerry.endswith('y')) # Output: True
print(jerry.isalpha()) # Output: True
print(jerry.islower()) # Output: False
print(jerry.isupper()) # Output: False
print(jerry.isspace()) # Output: False
print(jerry.split('e')) # Output: ['J', 'rry']
print(jerry.find('r')) # Output: 2
print(jerry.index('e')) # Output: 1


# Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:quote = '“The only way to do great work is to love what you do.”'
author = "Steve Jobs"
quote = '“The only way to do great work is to love what you do.”'
print(f'{author} once said, {quote}') # Output: Steve Jobs once said, “The only way to do great work is to love what you do.”



name = "  Al\nice Won\t derland.  "
print(name) # Output: "  Al\nice Won\t derland.  "
print(name.lstrip())
print(name.rstrip())
print(name.strip())
