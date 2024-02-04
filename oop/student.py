class Student:
    def __init__(self, name, house, petronus):
        if not name:
            raise ValueError("Name is required")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid House")
        self.name = name
        self.house = house 
        self.petronus = petronus
        
    def __str__(self):
        return f"{self.name} is in {self.house} and has a {self.petronus} petronus."

    def charm(self):
        match self.petronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Phoenix":
                return "🦅"
            case "Hare":
                return "🐰"
            case _:
                return "I don't know that spell"

def main():
    student = get_student()
    print(student)
    print(student.charm())
   
    
def get_student():
    name = input("Name: ").capitalize()
    house = input("House: ").capitalize()
    petronus = input("Petronus: ").capitalize()
    return Student(name, house, petronus)
    
    
if __name__ == "__main__":
    main()
    