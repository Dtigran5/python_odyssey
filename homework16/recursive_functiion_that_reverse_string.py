def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]

string = "hello"
print(f"reversed string of {string} is {reverse_string(string)}")
