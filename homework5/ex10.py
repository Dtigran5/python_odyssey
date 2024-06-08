tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

message = '''
This is a multi-line string
that uses single quotes.
It's easier to include "double quotes" without escaping.
'''

print(message)


name = "John"
age = 30
city = "New York"

complex_format = f'''
Hello {name}! 

Welcome to {city}. 

You are {age} years old. 

Here are some escape sequences:
1. Newline: \\n
2. Tab: \\t
3. Backslash: \\\\
'''

print(complex_format)
