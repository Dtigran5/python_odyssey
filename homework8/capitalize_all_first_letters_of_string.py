string = "hello, world! are you ready?"
title_case = ""
capitalize_next = True

for char in string:
    if char.isalpha():
        if capitalize_next:
            title_case += chr(ord(char) - 32)
            capitalize_next = False
        else:
            title_case += char
    else:
        title_case += char
        capitalize_next = True

print(title_case)
