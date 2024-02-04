# with open("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.csv") as file:
#     for line in file:
#         navn, eldre = line.strip().split(",")
#         # print(row)
#         print(f"{navn} is {eldre} kid")

unger = []

with open("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.csv") as file:
    for line in file:
        name, old = line.strip().split(",")
        unge = {"name": name, "onkel": old}
        unger.append(unge)

for unge in sorted(unger, key=lambda unger: unger['name']):
    print(f"{unge['name']} is {unge['onkel']} kid")
    
