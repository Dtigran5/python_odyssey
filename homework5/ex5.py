name = 'Tigran Daghbahsyan'
age = 19
height = 72 
weight = 179
eyes = 'Green'
teeth = 'White'
hair = 'Blavk'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

inches_to_cm = 2.54
pounds_to_kg = 0.4

inches = 10
pounds = 20

centimeters = inches * inches_to_cm
kilograms = pounds * pounds_to_kg

print(f"{inches} inches is equal to {centimeters} centimeters.")
print(f"{pounds} pounds is equal to {kilograms} kilograms.")
