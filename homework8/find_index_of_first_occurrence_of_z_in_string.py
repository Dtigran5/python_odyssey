s = "find the letter z"
found = False

for index in range(len(s)):
    if s[index] == 'z':
        print(f'The first occurrence of "z" is at index: {index}')
        found = True
        break
    
if not found:
    print('Character not found')
