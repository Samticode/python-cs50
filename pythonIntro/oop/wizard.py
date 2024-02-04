class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required")
        self.name = name

    def __str__(self):
        return f"{self.name} is a wizard."

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
    def __str__(self):
        return f"{self.name} is in {self.house} house."
        
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def __str__(self):
        return f"{self.name} teaches {self.subject}."
        
wizard = Wizard("Harry")
student = Student("Hermione", "Gryffindor")
professor = Professor("Snape", "Potions")

print(wizard, student, professor)