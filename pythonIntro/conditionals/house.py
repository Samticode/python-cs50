name = input("What is your name? ").title()

# if name == "Harry" or name == "Ron" or name == "Hermione":
#     print("Your house is Gryfinn!")
# elif name == "Draco":
#     print("Your house is Slytherin!")
# else:
#     print("Who?")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Your house is Gryfinn!")
    case "Draco":
        print("Your house is Slytherin!")
    case _:
        print("Who?")
