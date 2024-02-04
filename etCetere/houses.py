students = [
    {"name": "John", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Pansy", "house": "Slytherin"},
    {"name": "Zacharias", "house": "Hufflepuff"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Padma", "house": "Ravenclaw"},
    {"name": "Parvati", "house": "Gryffindor"},
]

houses = set()
for student in students:
    houses.add(student["house"])
        
for house in sorted(houses):
    print(house)