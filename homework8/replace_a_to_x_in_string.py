string = "banana"
replaced_str = ""

for char in string:
    if char == 'a':
        replaced_str += 'x'
    else:
        replaced_str += char
    
print(replaced_str)