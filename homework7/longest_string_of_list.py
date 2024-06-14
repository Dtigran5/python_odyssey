strings_list = ["hell", "day", "evening", "night"]
longest_index = 0
max_length = len(strings_list[0])

for i in range(1, len(strings_list)):
    if len(strings_list[i]) > max_length:
        longest_index = i
        max_length = len(strings_list[i])

print(f"Index of longest string: {longest_index}")
print(f"Longest string: {strings_list[longest_index]}")

