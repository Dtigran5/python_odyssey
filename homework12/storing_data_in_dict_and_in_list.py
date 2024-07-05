# Sample user data
user_data = [
    {"ID": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "password": "password123", "phone": "123-456-7890"},
    {"ID": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com", "password": "password456", "phone": "098-765-4321"},
]

user_dict = {}
user_list = []

for user in user_data:
    user_id = user["ID"]
    user_dict[user_id] = user
    user_list.append(user)

#1.searching in list
search_first_name = "Jane"
search_last_name = "Smith"
user_found = False

for user in user_list:
    if user["first_name"] == search_first_name and user["last_name"] == search_last_name:
        print("User found in list:")
        print(f"ID: {user['ID']}")
        print(f"First Name: {user['first_name']}")
        print(f"Last Name: {user['last_name']}")
        print(f"Email: {user['email']}")
        print(f"Password: {user['password']}")
        print(f"Phone: {user['phone']}")
        user_found = True
        break

if not user_found:
    print("Not found")

# 2.searching in dictionary
search_id = 2

if search_id in user_dict:
    user = user_dict[search_id]
    print("User found in dictionary:")
    print(f"ID: {user['ID']}")
    print(f"First Name: {user['first_name']}")
    print(f"Last Name: {user['last_name']}")
    print(f"Email: {user['email']}")
    print(f"Password: {user['password']}")
    print(f"Phone: {user['phone']}")
else:
    print("Not found in dictionary")
