import csv

# students = []

# with open("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
        
# for student in sorted(students, key= lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

name = input("Name: ")
home = input("Home: ")

with open ("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})