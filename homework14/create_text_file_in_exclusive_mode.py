try:
    with open('exclusive_mode.txt', 'x') as file:
        file.write("This is an exclusive mode file.")
except FileExistsError:
    print("FileExistsError: The file exclusive_mode.txt already exists.")
