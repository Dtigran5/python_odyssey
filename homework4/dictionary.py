students = {'Alice': 85, 'Bob': 90, 'Charlie': 88}
students['David'] = 92

for name, grade in students.items():
    print(f'{name}: {grade}')

students['Bob'] = 95
print(students)

students.pop('Charlie')
print(students)