class Cat:
    MEOWS = 300
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meow!")
            
cat = Cat()
cat.meow()