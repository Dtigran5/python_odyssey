my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count_dict = {item: my_list.count(item) for item in my_list}

for key, value in count_dict.items():
    print(f'{key}: {value}')
