class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, and {self.knuts} knuts."
        
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
        
potter = Vault(100, 10, 42)
print(potter)

weasley = Vault(50, 5, 21)
print(weasley)

granger = Vault(25, 2, 7)
print(granger)

total = potter + weasley + granger
print(total)