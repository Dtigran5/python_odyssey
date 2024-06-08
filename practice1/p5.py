ls = [1,2,3,4]
max = ls[0]
min = ls[0]

for i in ls:
    if i > max:
        max = i
print(f"this is max: {max}")

for j in ls:
    if j < min:
        min = j
print(f"this is min: {min}")

sum = max + min
print(f"the sum of max and min is: {sum}")