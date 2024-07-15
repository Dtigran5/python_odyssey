def first_uppercase_letter(string):
    for char in string:
        if char.isupper():
            return char
    return None


string = "hello World"
print(first_uppercase_letter(string))