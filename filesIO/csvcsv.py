import csv

families = []

with open("/Users/samtiahmed/Desktop/VG2/Utvikling/python/cs550/filesIO/names.csv") as file:
    reader = csv.reader(file)
    for nevau, voksen in reader:
        families.append({"Nevøen": nevau, "Voksen": voksen})
        
for nev in sorted(families, key=lambda families: families['Nevøen']):
    print(f"{nev['Nevøen']} errrr {nev['Voksen']} kid")