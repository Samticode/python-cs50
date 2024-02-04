# names = []

# for _ in range(3):
#     names.append(input("Enter a name: "))
    
# for name in sorted(names):
#     print(f"{name} is awesome!")



# name = input("Enter a name: ")

# with open("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.txt", "a") as file:
#     file.write(f"{name}\n")



# with open("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.txt", "r") as file:
#     for line in file:
#         print(f"{line.strip()} is awesome!")
        
        

names = []

with open("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names, reverse=True):
    print(f"{name} is awesome!")