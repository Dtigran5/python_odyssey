def print_characters(string, index=0):
    if index >= len(string):
        return
    print(string[index])
    print_characters(string, index + 1)

string = "Hello, World!"
print_characters(string)
