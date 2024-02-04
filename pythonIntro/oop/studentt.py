class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name is required")
        self.name = name
        self.house = house 
        
    def __str__(self):
        return f"{self.name} is in {self.house} house."
    
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        if not name:
            raise ValueError("Name is required")
    
    @property
    def house(self):
        return self._house 

    @house.setter
    def house(self, house):
        self._house = house


def main():
    student = get_student() 
    print(student)
   
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student
    
    
if __name__ == "__main__":
    main()