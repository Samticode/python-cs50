# students = ['Harry', 'Ron', 'Hermione']

# for i in range(len(students)):
#     print(students[i])
    
# for i in students:
#     print(i)

# students = {
#     "Harry": "Gryffindor",
#     "Draco": "Slytherin",
#     "Luna": "Ravenclaw",
#     "Cho": "Ravenclaw",
#     "Cedric": "Hufflepuff",
#     "Pansy": "Slytherin",
#     "Padma": "Ravenclaw",
# }

# for student in students:
#     print(student ,students[student], sep=": ")

students = [
    {"name": "Harry", "house": "Gryffindor", "petronus": "Stag"},
    {"name": "Cho", "house": "Ravenclaw", "petronus": "Swan"},
    {"name": "Draco", "house": "Slytherin", "petronus": None},
    {"name": "Luna", "house": "Ravenclaw", "petronus": "Hare"},
    {"name": "Ginny", "house": "Gryffindor", "petronus": "Horse"},
]

for student in students:
    print(f'Name: {student["name"]} \nHouse: {student["house"]} \nPetronus: {student["petronus"]} \n')