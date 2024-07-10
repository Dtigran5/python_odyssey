with open('specific_position.txt', 'r+') as file:
    content = file.read()
    file.seek(0)  
    file.write('Initial Text\n')  
    specific_position = 15  
    file.seek(specific_position)  
    file.write('Text at Specific Position')  
